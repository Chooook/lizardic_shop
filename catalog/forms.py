from django import forms

from .models import (
    Item,
    Category,
    SubCategory,
)


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = (
            'item_name',
            'price',
            'stock',
            'available',
            'category',
            'subcategory',
            'item_description',
            'image'
        )

    item_name        = forms.CharField(label='Item name', max_length=250)
    price            = forms.IntegerField(
        label='Price',
        min_value=0,
        initial=1000
    )
    stock            = forms.IntegerField(
        label='Stock',
        min_value=0,
        initial=1
    )
    available        = forms.BooleanField(label='Availability', initial=True)
    category         = forms.ModelChoiceField(
        label='',
        queryset=Category.objects.all(),
        widget=forms.Select,
        # FIXME ломает миграции, найти решение:
        #  Возможное решение - хранение категорий не в бд, а как переменную
        # initial=Category.objects.first()
    )
    subcategory      = forms.ModelChoiceField(
        label='',
        queryset=SubCategory.objects.all(),
        widget=forms.Select,
        # FIXME ломает миграции, найти решение:
        # initial=SubCategory.objects.first()
    )
    item_description = forms.CharField(
        label='Item description',
        widget=forms.Textarea,
        required=False
    )
    image            = forms.ImageField(allow_empty_file=True, required=False)


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('category_name', )

    category_name = forms.CharField(label='Category name')


class SubCategoryForm(forms.ModelForm):

    class Meta:
        model = SubCategory
        fields = ('subcategory_name', 'parent_category')

    subcategory_name = forms.CharField(label='Subcategory name')
    parent_category  = forms.ModelChoiceField(
        label='',
        queryset=Category.objects.all(),
        widget=forms.Select,
        # FIXME ломает миграции, найти решение:
        # initial=Category.objects.first()
    )
