from rest_framework import generics

from app.common import OwnedByUserMixin, ProtectedDeleteMixin
from account.models import AccountModel
from account.serializers import AccountSerializer

class AccountListCreateView(OwnedByUserMixin, ProtectedDeleteMixin, generics.ListCreateAPIView):
    queryset = AccountModel.objects.all()
    serializer_class = AccountSerializer

class AccountRetrieveUpdateDestroyView(OwnedByUserMixin, ProtectedDeleteMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = AccountModel.objects.all()
    serializer_class = AccountSerializer
