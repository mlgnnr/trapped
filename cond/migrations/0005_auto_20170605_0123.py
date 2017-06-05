# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-05 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cond', '0004_weatherstation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherstation',
            name='humidity',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='weatherstation',
            name='temp',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='weatherstation',
            name='temp_road',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
