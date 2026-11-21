from django.urls import path
from account.views import AccountListCreateView, AccountRetrieveUpdateDestroyView

urlpatterns = [
    path('account/', AccountListCreateView.as_view(), name='account-create-list'),
    path('account/<int:pk>/', AccountRetrieveUpdateDestroyView.as_view(), name='account-detail-view'),
]
