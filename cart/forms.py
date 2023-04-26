from django import forms

from catalog.models import Item
from cart.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('item', 'quantity', 'address', 'phone', 'status')

    item = forms.ModelChoiceField(
        label='',
        queryset=Item.objects.filter(available=True),
        widget=forms.Select,
        # FIXME ломает миграции, найти решение:
        #  Возможное решение - хранение категорий не в бд, а как переменную
        # initial=Item.objects.filter(available=True).first()
    )
    quantity = forms.IntegerField(min_value=1, label='Quantity')
    address = forms.CharField(label='Address to deliver to')
