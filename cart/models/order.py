from django.db import models

from user.models import MyUser


class Order(models.Model):

    user        = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    first_name  = models.CharField(
        max_length=50
    )
    last_name   = models.CharField(
        max_length=50
    )
    email       = models.EmailField(
        max_length=100
    )
    address     = models.CharField(
        max_length=200,
        default='',
        blank=True
    )
    # TODO Сделать, чтобы были только цифры:
    #  Возможное решение - библиотека django-phonenumber-field
    phone       = models.CharField(
        max_length=12,
        default='',
        blank=True
    )
    total_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True
    )
    created_at  = models.DateField(
        auto_now_add=True
    )
    status      = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return 'Заказ №%s от: %s, заказчик: %s' % (
            self.id,
            self.created_at,
            self.user,
        )
