from rest_framework import serializers
from account.models import AccountModel

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountModel
        fields = ["id", "name", "type", "initial_balance"]

    def validate_name(self, value):
        user = self.context["request"].user
        qs = AccountModel.objects.filter(user=user, name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError(
                "Você já tem uma conta com esse nome."
            )
        return value