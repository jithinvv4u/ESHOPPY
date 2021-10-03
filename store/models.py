from django.db import models

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    price=models.IntegerField()
    stock=models.IntegerField()
    description=models.TextField(max_length=50)
    image=models.ImageField(upload_to='static/images')