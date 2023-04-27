import djoser.urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView
from rest_framework import routers

from cart_api.urls import router as cart_api_router
from catalog_api.urls import router as category_api_router
from user.forms import MyUserForm


router = routers.DefaultRouter()
router.registry.extend(cart_api_router.registry)
router.registry.extend(category_api_router.registry)
router.registry.extend(djoser.urls.base.router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path(
        'users/register/',
        RegistrationView.as_view(form_class=MyUserForm),
        name='django_registration_register'
    ),
    path('users/', include('django_registration.backends.one_step.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('catalog.urls')),
    path('', include('cart.urls')),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
