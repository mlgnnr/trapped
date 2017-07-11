# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Road, Condition, Weather
from .models import WeatherStation, WeatherForecast, Image

from django.contrib import admin

# Register your models here.
admin.site.register(Road)
admin.site.register(Condition)
admin.site.register(Weather)
admin.site.register(WeatherStation)
admin.site.register(WeatherForecast)
admin.site.register(Image)
