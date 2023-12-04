from django.db import models

# Create your models here.

class Manager_Signup(models.Model):
    mname=models.CharField(max_length=50)
    memail=models.EmailField()
    mloc=models.CharField(max_length=100)
    mpass=models.CharField(max_length=50)
    mphone=models.IntegerField(default=0)
    status=models.IntegerField(default=0)