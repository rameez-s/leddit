# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-06 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dp',
            field=models.URLField(default='https://jennstrends.com/wp-content/uploads/2013/10/bad-profile-pic-2.jpeg', max_length=300),
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.URLField(default='https://www.linkedin.com/', max_length=300),
        ),
    ]
