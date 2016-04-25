from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=128)
    totalpoint = models.FloatField()
    type = models.CharField(max_length=128)
    begin_date = models.DateTimeField()
    memo = models.CharField(max_length=128)
