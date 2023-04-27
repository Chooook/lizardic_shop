from rest_framework import viewsets

from cart_api.models import Cart
from cart_api.serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
