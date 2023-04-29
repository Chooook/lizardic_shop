from rest_framework import serializers

from .models import Category, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'id',
            'item_name',
            'price',
            'stock',
            'available',
            'category',
            'item_description',
            'get_image',
            'get_thumbnail',
            'absolute_url'
        )


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'category_name',
            'absolute_url',
            'items'
        )
