from django.contrib.auth.mixins import PermissionRequiredMixin
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


class CategoryCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'admin'
    model = Category
    success_url = reverse_lazy('catalog:category-list')
    form_class = CategoryForm


class CategoryListView(ListView):
    model = Category
    context_object_name = 'category_list'


class CategoryDetailView(DetailView):
    model = Category


class CategoryUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'admin'
    model = Category
    success_url = reverse_lazy('catalog:category-list')
    form_class = CategoryForm


class CategoryDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'admin'
    model = Category
    success_url = reverse_lazy('catalog:category-list')
