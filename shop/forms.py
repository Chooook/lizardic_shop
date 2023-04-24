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
    price            = forms.IntegerField(label='Price', min_value=0)
    stock            = forms.IntegerField(label='Stock', min_value=0)
    available        = forms.BooleanField(label='Availability')
    category         = forms.ModelChoiceField(
        label='',
        queryset=Category.objects.all(),
        widget=forms.Select,
    )
    subcategory      = forms.ModelChoiceField(
        label='',
        queryset=SubCategory.objects.all(),
        widget=forms.Select,
    )
    item_description = forms.CharField(
        label='Item description',
        widget=forms.Textarea,
        required=False
    )
    image            = forms.ImageField(allow_empty_file=True)


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
    )
