from rest_framework import authentication, views, permissions
from rest_framework.response import Response

from cart_api.models import Order
from cart_api.serializers import OrderSerializer


class OrdersListView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
