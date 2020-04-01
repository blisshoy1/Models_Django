from django.db import models


# Create your models here.

class Info(models.Model):
    summary = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='images')
