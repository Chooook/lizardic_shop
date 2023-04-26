from django.contrib import admin
from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView

from user.forms import MyUserForm


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
]
