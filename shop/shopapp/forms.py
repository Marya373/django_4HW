from django import forms
from shopapp.models import Product

class LoadImageForProduct(forms.Form):

    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.Select(attrs={'class': 'form-control'})),
                                     
    image = forms.IntegerField(widget=forms.FileInput())

