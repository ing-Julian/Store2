from django.db import models 
from .product import Product
from .bill import Bill
from .client import Client

class Sale(models.Model):
    # id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    bill = models.ForeignKey(Bill, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
