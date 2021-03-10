import service as service
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

from datetime import date

from home.models import register



class appo(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=100)

class Book(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=100)

class Booking(models.Model):
    objects = None
    STATUS = (
        ('Pending', 'Pending'),
        ('Booked', 'Booked'),
    )
    customer = models.ForeignKey(register, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    date = models.DateField()
    time = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    beautician = models.CharField(max_length=100,default='Arif Balvar')
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.service



