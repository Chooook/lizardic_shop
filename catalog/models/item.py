from django.db import models
from django.utils.functional import cached_property
from django.utils.text import slugify

from catalog.models import Category


class Item(models.Model):
    item_name        = models.CharField(
        unique=True,
        max_length=250,
        help_text='Название позиции'
    )
    slug             = models.SlugField(
        unique=True,
        blank=True,
        max_length=250,
        help_text='Текст для ссылки'
    )
    price            = models.PositiveSmallIntegerField(
        default=1000,
        help_text='Цена'
    )
    stock            = models.PositiveSmallIntegerField(
        default=1,
        help_text='Количество в наличии'
    )
    available        = models.BooleanField(
        default=True,
        help_text='Доступность для заказа'
    )
    category         = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='items'
    )
    item_description = models.TextField(
        default='',
        blank=True,
        null=True,
        help_text='Описание позиции'
    )
    image            = models.ImageField(
        upload_to='media/items_images/',
        blank=True
    )

    @cached_property
    def absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)

    def __str__(self):
        return self.item_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.item_name)
        super(Item, self).save(*args, **kwargs)

    # @staticmethod
    # def get_all_items_by_category_name(category_name):
    #     if category_name:
    #         return Item.objects.filter(category__category_name=category_name)
    #     else:
    #         return Item.objects.all()
