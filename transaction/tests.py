from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from account.models import AccountModel
from category.models import CategoryModel
from transaction.models import TransactionModel

User = get_user_model()


class FinanceApiTests(APITestCase):
    def setUp(self):
        self.ana = User.objects.create_user("ana", password="123456")
        self.bia = User.objects.create_user("bia", password="123456")
        self.cat_ana = CategoryModel.objects.create(user=self.ana, name="Mercado")
        self.cat_bia = CategoryModel.objects.create(user=self.bia, name="Lazer")
        self.acc_bia = AccountModel.objects.create(
            user=self.bia, name="Nubank", type="checking"
        )
        self.client.force_authenticate(self.ana)

    def payload(self, **extra):
        data = {
            "category": self.cat_ana.id,
            "description": "Compras",
            "amount": "50.00",
            "type": "expense",
            "date": "2026-11-20T10:00:00Z",
        }
        data.update(extra)
        return data

    def test_exige_login(self):
        self.client.force_authenticate(None)
        for url in ("/api/v1/category/", "/api/v1/account/", "/api/v1/transaction/"):
            self.assertIn(self.client.get(url).status_code, (401, 403))

    def test_usuario_so_ve_os_proprios_dados(self):
        resp = self.client.get("/api/v1/category/")
        self.assertEqual([c["name"] for c in resp.data], ["Mercado"])
        resp = self.client.get(f"/api/v1/category/{self.cat_bia.id}/")
        self.assertEqual(resp.status_code, 404)

    def test_dono_e_definido_pelo_servidor(self):
        resp = self.client.post("/api/v1/transaction/", self.payload(), format="json")
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(TransactionModel.objects.get().user, self.ana)

    def test_nao_aceita_categoria_de_outro_usuario(self):
        resp = self.client.post(
            "/api/v1/transaction/",
            self.payload(category=self.cat_bia.id),
            format="json",
        )
        self.assertEqual(resp.status_code, 400)
        self.assertIn("category", resp.data)

    def test_nao_aceita_conta_de_outro_usuario(self):
        resp = self.client.post(
            "/api/v1/transaction/",
            self.payload(account=self.acc_bia.id),
            format="json",
        )
        self.assertEqual(resp.status_code, 400)
        self.assertIn("account", resp.data)

    def test_conta_e_opcional(self):
        resp = self.client.post("/api/v1/transaction/", self.payload(), format="json")
        self.assertEqual(resp.status_code, 201)
        self.assertIsNone(resp.data["account"])

    def test_valor_deve_ser_positivo(self):
        resp = self.client.post(
            "/api/v1/transaction/", self.payload(amount="0"), format="json"
        )
        self.assertEqual(resp.status_code, 400)

    def test_nome_repetido_retorna_400(self):
        resp = self.client.post(
            "/api/v1/category/", {"name": "mercado"}, format="json"
        )
        self.assertEqual(resp.status_code, 400)

    def test_mesmo_nome_em_outro_usuario_e_permitido(self):
        resp = self.client.post("/api/v1/category/", {"name": "Lazer"}, format="json")
        self.assertEqual(resp.status_code, 201)

    def test_apagar_categoria_com_lancamentos_retorna_409(self):
        self.client.post("/api/v1/transaction/", self.payload(), format="json")
        resp = self.client.delete(f"/api/v1/category/{self.cat_ana.id}/")
        self.assertEqual(resp.status_code, 409)

    def test_str_do_lancamento(self):
        self.client.post("/api/v1/transaction/", self.payload(), format="json")
        self.assertEqual(str(TransactionModel.objects.get()), "Compras (50.00)")
