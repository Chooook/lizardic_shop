from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('catalog.urls')),
    path('', include('cart.urls')),
]
