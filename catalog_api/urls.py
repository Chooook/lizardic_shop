from django.urls import include, path
from rest_framework import routers

from catalog_api import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryReadOnlyViewSet)
router.register(r'categories', views.CategoryModelViewSet)
router.register(r'items', views.ItemReadOnlyViewSet)
router.register(r'items', views.ItemModelViewSet)

urlpatterns = [
   path('api/', include(router.urls)),
]
