from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'item', ItemViewSet)

urlpatterns = [
   path('api/', include(router.urls)),
]
