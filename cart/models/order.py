from django.db import models

from cart.models import Cart
from user.models import MyUser


class Order(models.Model):

    user       = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    cart       = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='order'
    )
    address    = models.CharField(
        max_length=100,
        default='',
        blank=True
    )
    # TODO Сделать, чтобы были только цифры:
    #  Возможное решение - библиотека django-phonenumber-field
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
        return 'Заказ №%s от: %s, заказчик: %s' % (
            self.created_at,
            self.user,
            self.pk
        )
