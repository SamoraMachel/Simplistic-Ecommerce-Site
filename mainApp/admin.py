from django.contrib import admin
from .models import Product, ProductType, Customer

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Customer)