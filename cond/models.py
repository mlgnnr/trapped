# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models


class Road (models.Model):
    name = models.CharField(max_length=200)
    condition = models.CharField(max_length=50)
    last_update = models.DateTimeField('Last Update')

    def __str__(self):
        return self.name


class WeatherStation (models.Model):
    name = models.CharField(max_length=200)
    wind = models.SmallIntegerField()
    wind_direction = models.CharField(max_length=10)
    wind_max = models.SmallIntegerField()
    temp = models.DecimalField(max_digits=3, decimal_places=1)
    temp_road = models.DecimalField(max_digits=3, decimal_places=1)
    humidity = models.DecimalField(max_digits=4, decimal_places=1)
    last_update = models.DateTimeField('Last Update')

    def __str__(self):
        return self.name
# Create your models here.
