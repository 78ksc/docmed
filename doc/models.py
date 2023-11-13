from django.db import models

# Create your models here.
class Doctor(models.Model):
    # user = models.ForeignKey(User,)
    pic = models.ImageField(upload_to='images/doc', blank=True, null =True)
    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    spec = models.CharField(max_length=120)
    edu = models.CharField(max_length=40)
    exp = models.IntegerField()