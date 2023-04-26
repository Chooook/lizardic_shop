from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from cart.models import Order
from cart.forms import OrderForm


class OrderCreateView(CreateView):
    model = Order
    success_url = reverse_lazy('catalog:order-list')
    form_class = OrderForm


class OrderListView(ListView):
    model = Order
    context_object_name = 'order_list'


class OrderDetailView(DetailView):
    model = Order


class OrderUpdateView(UpdateView):
    model = Order
    success_url = reverse_lazy('catalog:order-list')
    form_class = OrderForm


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('catalog:order-list')
