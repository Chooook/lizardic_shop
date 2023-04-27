from rest_framework import viewsets

from catalog.models import Category
from catalog_api.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
