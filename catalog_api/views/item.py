from rest_framework import viewsets

from catalog.models import Item
from catalog_api.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
