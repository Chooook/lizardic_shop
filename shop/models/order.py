from django.db import models

from shop.models import Item


class Order(models.Model):

    item       = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )
    quantity   = models.PositiveSmallIntegerField(
        default=1
    )
    address    = models.CharField(
        max_length=100,
        default='',
        blank=True
    )
    phone      = models.CharField(
        max_length=12,
        default='',
        blank=True
    )
    created_at = models.DateField(
        auto_now_add=True
    )
    status     = models.BooleanField(
        default=False
    )

    def __str__(self):
        return '{} x{} at {}'.format(
            self.item.item_name,
            self.quantity,
            self.created_at
        )
