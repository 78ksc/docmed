# doc/models.py
from django.db import models
from client.models import Client
from med.models import Medicen, Investigation

class Doctor(models.Model):
    pic = models.ImageField(upload_to='images/doc', blank=True, null=True)
    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    spec = models.CharField(max_length=120)
    edu = models.CharField(max_length=40)
    exp = models.IntegerField()

# class Docsuggest(models.Model):
#     client = models.ForeignKey('client.Client', on_delete=models.CASCADE, null=True, blank=True)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
#     prescriptions = models.ManyToOneRel('med.Medicen', related_name='prescriptions')
#     investigations = models.ManyToOneRel('med.Investigation', related_name='investigations')


class Docsuggest(models.Model):
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    prescriptions = models.ManyToManyField('med.Medicen', related_name='prescriptions')
    investigations = models.ManyToManyField('med.Investigation', related_name='investigations')


class Presc(models.Model):
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    docsuggest = models.ForeignKey(Docsuggest, on_delete=models.CASCADE, null=True, blank=True)
    # med = models.ForeignKey('med.Medicen', on_delete=models.CASCADE, null=True, blank=True)

class Inves(models.Model):
    docsuggest = models.ForeignKey(Docsuggest, on_delete=models.CASCADE, null=True, blank=True)
    # inves = models.ForeignKey('med.Investigation', on_delete=models.CASCADE, null=True, blank=True)
