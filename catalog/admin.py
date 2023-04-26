from django.contrib import admin

from .models import (
    Item,
    Category,
    SubCategory
)


@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
    list_display = (
        'item_name',
        'slug',
        'price',
        'stock',
        'available',
        'category',
        'subcategory',
    )
    prepopulated_fields = {'slug': ('item_name', )}


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'slug',
        'display_subcategories',
        'display_items'
    )
    prepopulated_fields = {'slug': ('category_name', )}

    def display_subcategories(self, obj):
        subcategories = obj.subcategories.values_list(
            'subcategory_name',
            flat=True
        )
        return '; '.join(subcategories)
    display_subcategories.short_description = 'related subcategories'

    def display_items(self, obj):
        items = obj.items.values_list(
            'item_name',
            flat=True
        )
        return '; '.join(items)
    display_items.short_description = 'related items'


@admin.register(SubCategory)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = (
        'subcategory_name',
        'slug',
        'parent_category',
        'display_items'
    )
    prepopulated_fields = {'slug': ('subcategory_name', )}

    def display_items(self, obj):
        items = obj.items.values_list(
            'item_name',
            flat=True
        )
        return '; '.join(items)
    display_items.short_description = 'related items'
