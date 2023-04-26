from django import forms

from .models import (
    Item,
    Category,
    SubCategory,
    Order,
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
        initial=Category.objects.first()
    )
    subcategory      = forms.ModelChoiceField(
        label='',
        queryset=SubCategory.objects.all(),
        widget=forms.Select,
        initial=SubCategory.objects.first()
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
        initial=Category.objects.first()
    )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('item', 'quantity', 'address', 'phone', 'status')

    item = forms.ModelChoiceField(
        label='',
        queryset=Item.objects.filter(available=True),
        widget=forms.Select,
        initial=Item.objects.filter(available=True).first()
    )
    quantity = forms.IntegerField(min_value=1, label='Quantity')
    address = forms.CharField(label='Address to deliver to')
