from statistics import mode
from django.db import models

class Familiares(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.CharField(max_length=40)
    
