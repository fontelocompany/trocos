from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
class Families(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now=True, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, null=False)
    currency = models.CharField(null=False, max_length=3, default="EUR")

class User(AbstractUser):
    family = models.ForeignKey(Families, on_delete=models.CASCADE, null=True) # needs to have null=false
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(null=False, max_length=150)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email