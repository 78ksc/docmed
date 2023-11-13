from django.db import models

# Create your models here.
class Medicen(models.Model):
    pic = models.ImageField(upload_to='images/med', blank=True, null =True)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()