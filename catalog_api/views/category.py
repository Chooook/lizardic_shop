from django.http import Http404
from rest_framework import views
from rest_framework.response import Response

from catalog.models import Category
from catalog_api.serializers import CategorySerializer


class CategoryDetailView(views.APIView):

    @staticmethod
    def get_category(category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug):
        category = self.get_category(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
