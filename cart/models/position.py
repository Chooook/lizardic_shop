from django.db import models

from .order import Order
from catalog.models import Item


class Position(models.Model):

    order      = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    item       = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )
    price      = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    quantity   = models.PositiveSmallIntegerField(
        default=1
    )

    def __str__(self):
        return '%s' % self.id
