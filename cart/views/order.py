from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

# from cart.models import Position
# from cart.forms import OrderForm
#
#
# class OrderCreateView(CreateView):
#     model = Position
#     success_url = reverse_lazy('catalog:order-list')
#     form_class = OrderForm
#
#
# class OrderListView(ListView):
#     model = Position
#     context_object_name = 'order_list'
#
#
# class OrderDetailView(DetailView):
#     model = Position
#
#
# class OrderUpdateView(UpdateView):
#     model = Position
#     success_url = reverse_lazy('catalog:order-list')
#     form_class = OrderForm
#
#
# class OrderDeleteView(DeleteView):
#     model = Position
#     success_url = reverse_lazy('catalog:order-list')
