from django.urls import path
from category.views import CategoryListCreateView, CategoryRetrieveUpdateDestroyView

urlpatterns = [
    path('category/', CategoryListCreateView.as_view(), name='category-create-list'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail-view'),
]
