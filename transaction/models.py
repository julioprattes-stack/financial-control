from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from account.models import AccountModel
from category.models import CategoryModel

class TransactionModel(models.Model):
    class Type(models.TextChoices):
        INCOME = "income", "Receita"
        EXPENSE = "expense", "Despesa"
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions',
    )
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        related_name='transactions'
    )
    account = models.ForeignKey(
        AccountModel,
        on_delete=models.PROTECT,
        related_name="transactions",
        null=True,
        blank=True,
    )
    description = models.CharField(max_length=200)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    type = models.CharField(
        max_length=100,
        choices=Type.choices
    )
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.description} ({self.amount})"
    
