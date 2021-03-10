from django.db import models

# Create your models here.
class con(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=70, blank=2)
    website = models.CharField(max_length=20)
    message = models.TextField(max_length=100)
