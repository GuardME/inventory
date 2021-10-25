from django import forms
from django.forms import fields
from .models import Order, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_quantity']