from rest_framework import generics
from account.models import AccountModel
from account.serializers import AccountSerializer

class AccountListCreateView(generics.ListCreateAPIView):
    queryset = AccountModel.objects.all()
    serializer_class = AccountSerializer

class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccountModel.objects.all()
    serializer_class = AccountSerializer
