from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RowProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(required=False)
    price = forms.DecimalField(initial=199.99)
