from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=50)
    password=models.IntegerField()
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    DOB=models.IntegerField()
    address=models.CharField(max_length=100)
    phone_no=models.IntegerField()   
    created_on=models.DateTimeField()