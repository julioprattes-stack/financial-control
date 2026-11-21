from rest_framework import generics
from category.models import CategoryModel
from category.serializers import CategorySerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
