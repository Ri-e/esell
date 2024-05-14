from django.forms import ModelForm
from .models import Product
class createForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_desc', 'category', 'price', 'color_available', 'brand', 'modelname', 'opertingsys', 'cellulartech', 'images']
    