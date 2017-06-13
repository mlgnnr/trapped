# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-06 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cond', '0009_auto_20170605_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherstation',
            name='humidity',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='weatherstation',
            name='temp',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='weatherstation',
            name='temp_road',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
    ]