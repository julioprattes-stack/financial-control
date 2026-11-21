from rest_framework import generics
from transaction.models import TransactionModel
from transaction.serializers import TransactionSerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionSerializer

class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionSerializer
