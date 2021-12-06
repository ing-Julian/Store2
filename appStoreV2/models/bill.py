from django.db import models 

class Bill(models.Model):
    # id = models.AutoField(primary_key=True)
    date = models.DateField()
    total = models.IntegerField(default=0)
