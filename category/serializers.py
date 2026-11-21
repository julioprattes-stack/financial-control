from rest_framework import serializers
from category.models import CategoryModel

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ["id", "name"]

    def validate_name(self, value):
        user = self.context["request"].user
        qs = CategoryModel.objects.filter(user=user, name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError(
                "Você já tem uma categoria com esse nome."
            )
        return value