from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from catalog.models import Category
from catalog.forms import CategoryForm


class CategoryCreateView(CreateView):
    model = Category
    success_url = reverse_lazy('catalog:category-list')
    form_class = CategoryForm


class CategoryListView(ListView):
    model = Category
    context_object_name = 'category_list'


class CategoryDetailView(DetailView):
    model = Category


class CategoryUpdateView(UpdateView):
    model = Category
    success_url = reverse_lazy('catalog:category-list')
    form_class = CategoryForm


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('catalog:category-list')
