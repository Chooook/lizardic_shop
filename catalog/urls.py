from django.urls import path

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('',
         views.IndexTemplateView.as_view(),
         name='index'),
    path('items/create',
         views.ItemCreateView.as_view(),
         name='item-create'),
    path('items/list',
         views.ItemListView.as_view(),
         name='item-list'),
    path('items/detail/<slug:slug>',
         views.ItemDetailView.as_view(),
         name='item-detail'),
    path('items/update/<slug:slug>',
         views.ItemUpdateView.as_view(),
         name='item-update'),
    path('items/delete/<slug:slug>',
         views.ItemDeleteView.as_view(),
         name='item-delete'),
]
