from django.db import models


class Manager(models.Model):
    email=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    address=models.CharField(max_length=150)
    dob=models.DateField()
    company=models.CharField(max_length=100)

class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    email=models.EmailField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    company=models.CharField(max_length=30)
    mobile=models.PositiveBigIntegerField(unique=True)
    city=models.CharField(max_length=20)


# Create your models here.
