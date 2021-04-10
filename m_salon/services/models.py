from django.db import models


# Create your models here.
class service(models.Model):
    objects = None
    Service = models.CharField(max_length=20)
    Description = models.TextField()
    Catagory = models.CharField(max_length=10)
    price = models.FloatField()

    def __str__(self):
        return self.Service