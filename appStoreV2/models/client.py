from django.db import models 


class Client(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 100)
    lastname = models.CharField(max_length= 100)
    cedula = models.IntegerField(default=0)
    email = models.EmailField(max_length=100)