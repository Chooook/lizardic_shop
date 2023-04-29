from django.contrib import admin

from .models import (
    Position,
    Order,
)


@admin.register(Position)
class PositionModelAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'item',
        'price',
        'quantity',
    )


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'first_name',
        'last_name',
        'email',
        'address',
        'phone',
        'total_price',
        'created_at',
        'status',
    )
