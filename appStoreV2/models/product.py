from django.db import models 

class Product(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 100)
    price = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)
