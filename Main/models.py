from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    quatity = models.IntegerField(null=False, blank=False)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self):
        return self.name

