from django.conf import settings
from django.db import models

User : object = settings.AUTH_USER_MODEL

# Create your models here.
class ProductType(models.Model):
    type = models.CharField(max_length=20, null=False, blank=False)
    
    def __str__(self):
        return self.type

class Product(models.Model):
    image = models.ImageField(upload_to="productImages/")
    name = models.CharField(max_length=20, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    type = models.ForeignKey(ProductType, on_delete=models.deletion.CASCADE)
    quatity = models.IntegerField(null=False, blank=False)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.deletion.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.deletion.DO_NOTHING)
    quantity = models.IntegerField(null=False, blank=False)
    bought = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self):
        return f"{self.product} - {self.user}"
    
    @classmethod
    def create(cls, user, product, quantity):
        purchase = cls(user=user, product=product, quantity=quantity)
        purchase.save()
        
        return purchase
        
    
    
