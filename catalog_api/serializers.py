from rest_framework import serializers
from .models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'pk',
            'category_name',
            'absolute_url'
        )


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'pk',
            'item_name',
            'price',
            'stock',
            'available',
            'category',
            'item_description',
            'image',
            'absolute_url'
        )
