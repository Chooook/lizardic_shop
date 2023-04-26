from django.db import models
from django.utils.text import slugify

from catalog.models import Category


class SubCategory(models.Model):
    subcategory_name = models.CharField(
        unique=True,
        max_length=120,
        help_text='Название подкатегории'
    )
    slug             = models.SlugField(
        unique=True,
        blank=True,
        max_length=120,
        help_text='Текст для ссылки'
    )
    parent_category  = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='subcategories'
    )

    class Meta:
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.subcategory_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.subcategory_name)
        super(SubCategory, self).save(*args, **kwargs)
