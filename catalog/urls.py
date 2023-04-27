from django.urls import path

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('',
         views.IndexTemplateView.as_view(),
         name='index'),
    path('item/create',
         views.ItemCreateView.as_view(),
         name='item-create'),
    path('item/list',
         views.ItemListView.as_view(),
         name='item-list'),
    path('item/detail/<slug:slug>',
         views.ItemDetailView.as_view(),
         name='item-detail'),
    path('item/update/<slug:slug>',
         views.ItemUpdateView.as_view(),
         name='item-update'),
    path('item/delete/<slug:slug>',
         views.ItemDeleteView.as_view(),
         name='item-delete'),
]
