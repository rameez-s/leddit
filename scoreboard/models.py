# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

# Create your models here.

class User(models.Model):
    id_num = models.CharField(max_length = 200, default = "000")    
    pub_date = models.DateTimeField('date published', default = timezone.now())
    name = models.CharField(max_length = 200)
    headline = models.CharField(max_length = 250)
    score = models.IntegerField(default = 0)
    profile = models.URLField(max_length = 300, default = "https://www.linkedin.com/")
    dp = models.URLField(max_length = 300, default = "https://procurement.unl.edu/images/staff-photos/y_u_no_photo_Square.png")

    def __str__(self):
        return self.name
