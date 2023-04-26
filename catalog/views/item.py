from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from catalog.models import Item
from catalog.forms import ItemForm


class ItemCreateView(CreateView):
    model = Item
    success_url = reverse_lazy('catalog:item-list')
    form_class = ItemForm


class ItemListView(ListView):
    model = Item
    context_object_name = 'item_list'


class ItemDetailView(DetailView):
    model = Item


class ItemUpdateView(UpdateView):
    model = Item
    success_url = reverse_lazy('catalog:item-list')
    form_class = ItemForm


class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('catalog:item-list')
