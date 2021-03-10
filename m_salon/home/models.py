
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class register(models.Model):
    objects = None
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=70, blank=2)
    phone = models.CharField(max_length=10)
    profile_pic = models.ImageField(null=True, blank=True)
    password = models.CharField(max_length=8)
    confirm = models.CharField(max_length=8)

    def __str__(self):
        return self.username


    @staticmethod
    def get_customer_by_username(username):
        try:
            return register.objects.get(username=username)
        except:
            return False
