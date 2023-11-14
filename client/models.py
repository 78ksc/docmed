from django.db import models
from django.contrib.auth.forms import UserCreationForm
from doc.models import Doctor
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True)
    phone = models.IntegerField(blank=True,null=True)
    state = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=200,blank=True,null=True)
    pincode = models.IntegerField(blank=True,null=True)
    area = models.CharField(max_length=200,blank=True,null=True)
    dob = models.DateField(blank=True,null=True)

class Appoint(models.Model):
    request_created_by = models.ForeignKey(Client, on_delete=models.SET_NULL,null=True)
    pacient_name = models.CharField(max_length=40)
    pacient_age = models.IntegerField()
    pacient_addr = models.CharField(max_length=200)
    doctor_spec = models.CharField(max_length=120,blank=True)
    pacient_symptom = models.CharField(max_length=240)
    emergency = models.BooleanField(default=False,null=True)
    alloted_docto = models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True)

class DocAppoint(models.Model):
    booker = models.ForeignKey(Client,on_delete=models.DO_NOTHING,null=True,blank=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.DO_NOTHING,null=True,blank=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    alloted_time =  models.DateTimeField(null=True,blank=True)