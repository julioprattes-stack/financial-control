from rest_framework import generics

from app.common import OwnedByUserMixin
from transaction.models import TransactionModel
from transaction.serializers import TransactionSerializer

class TransactionListCreateView(OwnedByUserMixin, generics.ListCreateAPIView):
    queryset = TransactionModel.objects.select_related("category", "account")
    serializer_class = TransactionSerializer

class TransactionRetrieveUpdateDestroyView(OwnedByUserMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = TransactionModel.objects.select_related("category", "account")
    serializer_class = TransactionSerializer
