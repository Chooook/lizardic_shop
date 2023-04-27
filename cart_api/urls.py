from django.urls import include, path
from rest_framework import routers

from .views import CartViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
   path('api/', include(router.urls)),
]
