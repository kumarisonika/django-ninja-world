from statistics import mode
from django.db import models

class Village(models.Model):
    village_name=models.CharField(max_length=70, blank=False, default='')
    description=models.CharField(max_length=100)
    nation_id=models.IntegerField(max_length=5)
   


class Nation(models.Model):
    nation_name=models.CharField(max_length=70, blank=False, )
    element=models.CharField(max_length=70)
    kage_name=models.CharField(max_length=70, blank=False)
    description=models.CharField(max_length=100)




