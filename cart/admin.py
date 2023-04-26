from django.contrib import admin

from .models import (
    Position,
    Order,
    Cart
)


@admin.register(Position)
class PositionModelAdmin(admin.ModelAdmin):
    list_display = (
        'item',
        'quantity'
    )


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'cart',
        'address',
        'phone',
        'status'
    )


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'display_positions',
        'is_active'
    )

    def display_positions(self, obj):
        positions = obj.positions.values_list(
            'item__item_name',
            'quantity'
        )
        return '; '.join(
            '%s x%s' % pos for pos in positions
        )
    display_positions.short_description = 'related positions'

