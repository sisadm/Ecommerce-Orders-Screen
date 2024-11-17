from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'product_name', 'quantity']
        widget = {
            'customer_name': forms.TextInput(attrs={'class': 'm-2', 'placeholder': 'Enter customer Name:'}),
            'product_name': forms.TextInput(attrs={'class': 'm-2', 'placeholder': 'Enter product Name:'}),
            'quantity': forms.TextInput(attrs={'class': 'm-2', 'placeholder': 'Enter quantity:'})
        }