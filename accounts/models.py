from django.db import models
from users.models import Families

class Institutions(models.Model):
    name = models.TextField(null=False)
    logo = models.URLField() #TBD

    family = models.ForeignKey(Families, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Account(models.Model):
    family = models.ForeignKey(Families, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=100)
    account_type = models.TextField() # TBD

    balance = models.DecimalField(null=False, max_digits=14, decimal_places=2)
    currency = models.TextField(null=False)

    institution = models.CharField(null=False, max_length=150) # TBD
    is_active = models.BooleanField(null=False, default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)