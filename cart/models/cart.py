from django.db import models

from cart.models.position import Position
from user.models import MyUser


class Cart(models.Model):

    user      = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='carts'
    )
    positions = models.ManyToManyField(
        Position
    )
    is_active = models.BooleanField(
        default=True
    )

    def add_position(self, item, quantity):
        position = Position.objects.get_or_create(
            item_id=item,
            quantity=quantity
        )
        self.positions.add(position)

        return position

    def __str__(self):
        return ''.join(
            '%s x%s' % (pos.item, pos.quantity) for pos in self.positions.all()
        )
