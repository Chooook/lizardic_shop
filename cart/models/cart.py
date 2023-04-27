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
        if self.positions.filter(item_id=item.id).exists():
            old_position = self.positions.get(item_id=item.id)
            quantity += old_position.quantity
            self.positions.remove(old_position)

        position = Position.objects.get_or_create(
            item_id=item,
            quantity=quantity
        )
        self.positions.add(position)
        return self.positions

    def remove_position(self, position):
        if self.positions.filter(position=position).exists():
            self.positions.remove(position)
        return self.positions

    def __str__(self):
        return ''.join(
            '%s x%s' % (pos.item, pos.quantity) for pos in self.positions.all()
        )
