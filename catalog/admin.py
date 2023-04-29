from django.contrib import admin

from .models import (
    Item,
    Category,
)


@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'item_name',
        'slug',
        'price',
        'stock',
        'available',
        'item_description',
        'image',
        'thumbnail',
        'created_at',
        'absolute_url',
    )
    prepopulated_fields = {'slug': ('item_name', )}


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'slug'
    )
    prepopulated_fields = {'slug': ('category_name', )}

    def display_items(self, obj):
        items = obj.items.values_list(
            'item_name',
            flat=True
        )
        return '; '.join(items)
    display_items.short_description = 'related items'
