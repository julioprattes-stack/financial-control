from django.conf import settings
from django.db import models

class AccountModel(models.Model):
    class Type(models.TextChoices):
        CHECKING = "checking", "Conta corrente"
        SAVINGS = "savings", "Poupança"
        CASH = "cash", "Dinheiro"
        CREDIT_CARD = "credit_card", "Cartão de crédito"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="accounts",
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=Type.choices)
    initial_balance = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )

    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name"], name="unique_account_per_user"
            ),
        ]

    def __str__(self):
        return self.name