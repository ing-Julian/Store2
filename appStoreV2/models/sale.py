from django.db import models 

class Sale(models.Model):
    quantity = models.IntegerField(default=0)
    