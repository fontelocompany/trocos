from django.db import models

# Create your models here.
class Families(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now=True, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, null=False)
    currency = models.CharField(null=False, max_length=3, default="EUR")

class User(models.Model):
    family = models.ForeignKey(Families, on_delete=models.CASCADE, null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=False)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)