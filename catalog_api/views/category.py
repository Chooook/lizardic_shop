from rest_framework import viewsets, permissions

from catalog.models import Category
from catalog_api.serializers import CategorySerializer


class CategoryReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
