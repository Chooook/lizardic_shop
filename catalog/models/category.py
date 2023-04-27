from django.db import models
from django.utils.functional import cached_property
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(
        unique=True,
        max_length=120,
        help_text='Название категории'
    )
    slug          = models.SlugField(
        unique=True,
        blank=True,
        max_length=120,
        help_text='Текст для ссылки'
    )

    @cached_property
    def absolute_url(self):
        return '/%s/' % self.slug

    class Meta:
        ordering = ('category_name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
