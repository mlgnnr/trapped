# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models


class Road (models.Model):
    name = models.CharField(max_length=200)
    condition = models.CharField(max_length=50)
    last_update = models.DateTimeField('Last Update')

    def __str__(self):
        return self.Road.name
# Create your models here.
