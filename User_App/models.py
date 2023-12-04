from django.db import models
from Admin_App.models import *
from Manager_App.models import *

# Create your models here.

class Signup(models.Model):
    name=models.CharField(max_length=20)
    num=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=20)

class contact_dbs(models.Model):
    uname=models.CharField(max_length=20)
    uemail=models.EmailField()
    usubject=models.CharField(max_length=15)
    umessage=models.TextField()

class BookTurf(models.Model):
    userid=models.ForeignKey(Signup,on_delete=models.CASCADE)
    turfid=models.ForeignKey(turf_dbs,on_delete=models.CASCADE,default='')
    mid=models.ForeignKey(Manager_Signup,on_delete=models.CASCADE,null=True,default='')
    bookingdate=models.DateField()
    bstime=models.TimeField()
    betime=models.TimeField()
    duration=models.IntegerField()
    btotal=models.TextField()
    status=models.IntegerField(default=0)

