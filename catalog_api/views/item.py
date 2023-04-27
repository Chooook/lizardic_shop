from rest_framework import viewsets, permissions

from catalog.models import Item
from catalog_api.serializers import ItemSerializer


class ItemReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemModelViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser, )
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
