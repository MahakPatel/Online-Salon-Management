from django.db import models


# Create your models here.
class service(models.Model):
    Service = models.CharField(max_length=20)
    Description = models.TextField()
    Catagory = models.CharField(max_length=10)
    price = models.IntegerField()

    def __str__(self):
        return self.Service