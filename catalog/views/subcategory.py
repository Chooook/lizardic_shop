from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from catalog.models import SubCategory
from catalog.forms import SubCategoryForm


class SubCategoryCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'admin'
    model = SubCategory
    success_url = reverse_lazy('catalog:subcategory-list')
    form_class = SubCategoryForm


class SubCategoryListView(ListView):
    model = SubCategory
    context_object_name = 'subcategory_list'


class SubCategoryDetailView(DetailView):
    model = SubCategory


class SubCategoryUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'admin'
    model = SubCategory
    success_url = reverse_lazy('catalog:subcategory-list')
    form_class = SubCategoryForm


class SubCategoryDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'admin'
    model = SubCategory
    success_url = reverse_lazy('catalog:subcategory-list')
