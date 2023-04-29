from django.db.models import Q
from django.http import Http404
from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response

from catalog.models import Item
from catalog_api.serializers import ItemSerializer


class ItemDetailView(views.APIView):

    @staticmethod
    def get_item(category_slug, item_slug):
        try:
            return (
                Item.objects
                .filter(category__slug=category_slug)
                .get(slug=item_slug)
            )
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, item_slug):
        item = self.get_item(category_slug, item_slug)
        serializer = ItemSerializer(item)
        return Response(serializer.data)


class LatestItemsListView(views.APIView):

    @staticmethod
    def get(request):
        items = Item.objects.all()[0:5]
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')
    if query:
        items = Item.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
