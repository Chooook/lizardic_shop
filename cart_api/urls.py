from django.urls import path

from cart_api import views


urlpatterns = [
   path('orders/', views.OrdersListView.as_view()),
]
