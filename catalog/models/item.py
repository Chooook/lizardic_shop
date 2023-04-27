from io import BytesIO

from django.core.files import File
from django.db import models
from django.utils.functional import cached_property
from django.utils.text import slugify
from PIL import Image

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
        on_delete=models.CASCADE,
        related_name='items',
        help_text='Категория позиции'
    )
    item_description = models.TextField(
        blank=True,
        null=True,
        help_text='Описание позиции'
    )
    image            = models.ImageField(
        upload_to='media/items_images/',
        blank=True,
        null=True,
        help_text='Фото позиции'
    )
    thumbnail        = models.ImageField(
        upload_to='items_images/',
        blank=True,
        null=True,
        help_text='Фото позиции'
    )
    created_at       = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', 'item_name')

    @cached_property
    def absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)

    def __str__(self):
        return self.item_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.item_name)
        super(Item, self).save(*args, **kwargs)

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            return ''

    @staticmethod
    def make_thumbnail( image, size=(200, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

    # @staticmethod
    # def get_all_items_by_category_name(category_name):
    #     if category_name:
    #         return Item.objects.filter(category__category_name=category_name)
    #     else:
    #         return Item.objects.all()
