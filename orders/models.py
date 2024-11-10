from django.db import models
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=200)
    quantity  = models.IntegerField()
    order_date = models.DateTimeField(default=timezone.now)