from django.contrib import admin
from account.models import AccountModel

@admin.register(AccountModel)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "type")
