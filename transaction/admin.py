from django.contrib import admin
from transaction.models import TransactionModel

@admin.register(TransactionModel)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
    "user", "category", "account", "description", "amount", "type", "date", "created_at",
    )
