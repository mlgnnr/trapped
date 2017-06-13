# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Road, WeatherStation, RoadCondition

from django.contrib import admin

# Register your models here.
admin.site.register(Road)
admin.site.register(WeatherStation)
admin.site.register(RoadCondition)
