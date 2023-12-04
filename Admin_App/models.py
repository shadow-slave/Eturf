from django.db import models
from Manager_App.models import *
# Create your models here.
class LocMan(models.Model):
    locimage=models.ImageField(upload_to='location_img',default='')
    loc=models.TextField()

class admin_dbs(models.Model):
    aname=models.CharField(max_length=15)
    apass=models.CharField(max_length=15)

class turf_dbs(models.Model):
    tmanagerid=models.ForeignKey(Manager_Signup,on_delete=models.CASCADE,default=3)
    tname=models.CharField(max_length=100)
    tprice=models.IntegerField()
    tstime=models.TimeField()
    tetime=models.TimeField()
    tloc=models.CharField(max_length=25)
    tarea=models.CharField(max_length=100)
    taddress=models.URLField(max_length=500)
    features=models.TextField(default='')
    timage1=models.ImageField(upload_to='turf_img',default='')
    timage2=models.ImageField(upload_to='turf_img',default='')
    timage3=models.ImageField(upload_to='turf_img',default='')