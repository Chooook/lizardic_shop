from rest_framework import viewsets

from cart_api.models import Order
from cart_api.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
