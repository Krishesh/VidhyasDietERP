from django.db import models


# Create your models here.

class test(models.Model):
    test = models.CharField(max_length=10, default="")
    bibek = models.CharField(max_length=10, default="")
