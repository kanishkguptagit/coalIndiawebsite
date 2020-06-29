from django.db import models

# Create your models here.
class production(models.Model):
    date = models.DateField()
    actual_production = models.IntegerField()
    reported_production = models.IntegerField()

class transport(models.Model):
    date = models.DateField()
    transport_trip = models.IntegerField()
    dispatch = models.IntegerField()