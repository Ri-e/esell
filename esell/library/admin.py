from django.contrib import admin

# Register your models here.
from .models import Product, Comment, Category

admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Category)