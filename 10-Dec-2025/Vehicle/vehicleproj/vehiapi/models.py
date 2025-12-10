from django.db import models
class Vehicle_Manufacture(models.Model):
    number_plate = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    year = models.IntegerField()

def __str__(self):
    return self.number_plate

# Create your models here.
