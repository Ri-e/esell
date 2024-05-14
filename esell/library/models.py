from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    product_name = models.CharField(max_length=2000)
    product_desc = models.CharField(max_length=2000)
    category = models.CharField(max_length=500)
    price = models.IntegerField()
    color_available = models.CharField(max_length=500)
    buyers = models.ManyToManyField(User, related_name='buyers', blank=True)
    images = models.ImageField(upload_to='product_images/', default='', blank=True, null=True)
    brand = models.CharField(max_length=200, blank=True, null = True)
    modelname = models.CharField(max_length=200,blank=True, null = True)
    opertingsys = models.CharField(max_length=200,blank=True, null = True)
    cellulartech = models.CharField(max_length=200,blank=True, null = True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey(Product, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message[0:25] + "..."