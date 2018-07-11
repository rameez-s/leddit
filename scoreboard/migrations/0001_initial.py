# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-06 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('headline', models.CharField(max_length=250)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]