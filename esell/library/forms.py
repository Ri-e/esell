from django.forms import ModelForm
from .models import Product, Category
class createForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_desc', 'category', 'price', 'color_available', 'brand', 'modelname', 'opertingsys', 'cellulartech', 'images']
class createCats(ModelForm):
    class Meta:
        model = Category
        fields= "__all__"