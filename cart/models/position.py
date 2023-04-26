from django.db import models

from catalog.models import Item


class Position(models.Model):

    item       = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )
    quantity   = models.PositiveSmallIntegerField(
        default=1
    )

    def __str__(self):
        return '%s x%s' % (self.item, self.quantity)
