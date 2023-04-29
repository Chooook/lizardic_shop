from rest_framework import serializers
from .models import Position, Order


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = (
            'item',
            'price',
            'quantity'
        )


class OrderSerializer(serializers.ModelSerializer):
    items = PositionSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'address',
            'phone',
            'total_price',
            'items',
            'created_at',
            'status'
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            Position.objects.create(order=order, **item_data)

        return order
