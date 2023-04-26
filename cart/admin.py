from django.contrib import admin

from .models import (
    Order
)


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = (
        'item',
        'quantity',
        'address',
        'phone'
    )
