from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from django_registration.backends.one_step.views import RegistrationView
# from user.forms import MyUserForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    # path(
    #     'users/register/',
    #     RegistrationView.as_view(form_class=MyUserForm),
    #     name='django_registration_register'
    # ),
    # path('users/', include('django_registration.backends.one_step.urls')),
    # path('users/', include('django.contrib.auth.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('catalog_api.urls')),
    path('api/v1/', include('cart_api.urls')),
    path('', include('catalog.urls')),
    path('', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
