from django.db.models import ProtectedError
from rest_framework import serializers, status
from rest_framework.response import Response


class OwnedByUserMixin:
    """Cada usuário enxerga e cria apenas os próprios registros."""

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProtectedDeleteMixin:
    """Devolve 409 (e não 500) ao apagar algo que ainda tem lançamentos."""

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(
                {"detail": "Não é possível apagar: há lançamentos vinculados."},
                status=status.HTTP_409_CONFLICT,
            )


class UserOwnedPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    """Só aceita (e só lista) objetos que pertencem ao usuário logado."""

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.context.get("request")
        if queryset is None or request is None:
            return queryset.none() if queryset is not None else queryset
        return queryset.filter(user=request.user)
