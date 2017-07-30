# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models
from datetime import datetime

class Road (models.Model):
    name = models.CharField(max_length=200)
    id_butur = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.name

class Condition (models.Model):
    road = models.OneToOneField(Road,on_delete=models.CASCADE)
    status = models.CharField(blank=True, max_length=70)
    sign = models.IntegerField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.road.name

class Weather (models.Model):
    road = models.OneToOneField(Road,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return self.road.name

class WeatherStation (models.Model):
    road = models.OneToOneField(Weather,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=200)
    wind = models.SmallIntegerField(blank=True, null=True)
    wind_direction = models.CharField(blank=True, max_length=10)
    wind_max = models.DecimalField(max_digits=3, decimal_places=0)
    temp = models.DecimalField(max_digits=3, decimal_places=0)
    temp_road = models.DecimalField(max_digits=3, decimal_places=0)
    humidity = models.DecimalField(max_digits=3, decimal_places=0)
    last_update = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.name

class WeatherForecast (models.Model):
    weather = models.ForeignKey(Weather)
    name = models.CharField(max_length=200)
    hour = models.SmallIntegerField(blank=True, null=True)
    wind_direction = models.CharField(blank=True, max_length=10)
    wind = models.SmallIntegerField(blank=True, null=True)
    temp = models.DecimalField(max_digits=3, decimal_places=0)
    sky = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name

class Image (models.Model):
    road = models.ForeignKey(Road)
    url = models.CharField(max_length=200)
    image_id = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.road.name + '_' + str(self.image_id)
# Create your models here.
