from django import forms
from shopapp.models import Product

class ImageForm(forms.Form):

    
    image = forms.IntegerField(widget=forms.FileInput())