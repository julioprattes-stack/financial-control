from rest_framework import serializers

from app.common import UserOwnedPrimaryKeyRelatedField
from account.models import AccountModel
from category.models import CategoryModel
from transaction.models import TransactionModel

class TransactionSerializer(serializers.ModelSerializer):
    category = UserOwnedPrimaryKeyRelatedField(queryset=CategoryModel.objects.all())
    account = UserOwnedPrimaryKeyRelatedField(
        queryset=AccountModel.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = TransactionModel
        fields = [
            "id",
            "category",
            "account",
            "description",
            "amount",
            "type",
            "date",
            "created_at",
        ]
        read_only_fields = ["created_at"]