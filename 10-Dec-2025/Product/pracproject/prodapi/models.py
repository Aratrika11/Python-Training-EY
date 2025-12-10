from django.db import models
class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()

def __str__(self):
    return self.prod_name

# Create your models here.
