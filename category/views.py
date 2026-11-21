from rest_framework import generics

from app.common import OwnedByUserMixin, ProtectedDeleteMixin
from category.models import CategoryModel
from category.serializers import CategorySerializer

class CategoryListCreateView(OwnedByUserMixin, ProtectedDeleteMixin, generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(OwnedByUserMixin, ProtectedDeleteMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
