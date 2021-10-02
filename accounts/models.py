from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Customer(AbstractUser):
    phone=models.IntegerField()
# class Seller(AbstractUser):
#     phone=models.IntegerField(max_length=50)