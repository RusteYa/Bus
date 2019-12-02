from django.db import models


class Bus(models.Model):
    GaragNumb = models.IntegerField()
    Marsh = models.CharField(max_length=10)
    Graph = models.IntegerField()
    Smena = models.IntegerField()
    TimeNav = models.DateTimeField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Speed = models.IntegerField()
    Azimuth = models.IntegerField()
