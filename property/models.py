from django.db import models

# Create your models here.
class Car(models.Model):
    year = models.PositiveIntegerField(null=False) # limit by year from 1900 to current year
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=150)

    odometer_value = models.PositiveIntegerField(null=False)
    odometer_unit = models.TextField() # km or miles

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Residency(models.Model):
    type = models.TextField() # house, apartment, farm. change when frontend is implemented

    name = models.CharField(max_length=150, null=False)
    year_built = models.DateField(null=False)
    address = models.CharField(max_length=250)
    
    area_value = models.FloatField(null=False, default=0)
    area_unit = models.TextField() # m2 sq2 etc

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)