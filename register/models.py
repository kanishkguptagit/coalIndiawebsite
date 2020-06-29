from django.db import models

# Create your models here.
class details(models.Model):
    name = models.IntegerField()
    email = models.EmailField()
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    username = models.CharField(max_length=30)