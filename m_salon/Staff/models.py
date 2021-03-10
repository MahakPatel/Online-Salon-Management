from django.db import models

# Create your models here.
class Staff(models.Model):
    name=models.CharField(max_length=20)
    service=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.CharField(max_length=10)
    status=models.BooleanField()
    salary = models.IntegerField()
    def __str__(self):
        return self.name

