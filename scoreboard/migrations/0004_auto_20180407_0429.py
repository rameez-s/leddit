# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-07 01:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0003_auto_20180406_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id_num',
            field=models.CharField(default='000', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 1, 29, 54, 363029, tzinfo=utc), verbose_name='date published'),
        ),
    ]
