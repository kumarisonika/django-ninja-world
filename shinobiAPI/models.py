from statistics import mode
from django.db import models

class Village(models.Model):
    village_name=models.CharField(max_length=70, blank=False, default='')
    description=models.CharField(max_length=100)
    nation=models.CharField(max_length=100)
    kage_name=models.CharField(max_length=50)
    element=models.CharField(max_length=50)

   


class Nation(models.Model):
    nation_name=models.CharField(max_length=70, blank=False, )
    element=models.CharField(max_length=70)
    kage_name=models.CharField(max_length=70, blank=False)
    description=models.CharField(max_length=100)

class User(models.Model):
    username=models.CharField(max_length=70, blank=False, )
    salt=models.BinaryField(blank=False)
    hashed_password=models.BinaryField(blank=False)




