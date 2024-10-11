from django.db import models

# 
class Inflation(models.Model):
    country = models.TextField(null=False)
    value = models.DecimalField(decimal_places=1, max_digits=2, null=False)
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# Needs indexes
class ExchangeRate(models.Model):
    from_currency = models.TextField(null=False)
    to_currency = models.TextField(null=False)
    
    rate = models.DecimalField(null=False, max_digits=4, decimal_places=2)
    date = models.DateField(null=False)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)