from django.urls import path

from catalog_api import views


urlpatterns = [
    path('items/<slug:category_slug>/',
         views.CategoryDetailView.as_view()),
    path('items/<slug:category_slug>/<slug:item_slug>',
         views.ItemDetailView.as_view()),
    path('latest-items', views.LatestItemsListView.as_view()),
    path('items/search', views.search),
]
