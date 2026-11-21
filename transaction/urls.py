from django.urls import path
from transaction.views import TransactionListCreateView, TransactionRetrieveUpdateDestroyView

urlpatterns = [
    path('transaction/', TransactionListCreateView.as_view(), name='transaction-create-list'),
    path('transaction/<int:pk>/', TransactionRetrieveUpdateDestroyView.as_view(), name='transactio-detail-view'),
]
