# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-30 14:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cond', '0003_auto_20170729_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='last_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
