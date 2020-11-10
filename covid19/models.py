from django.db import models
from datetime import datetime
from django.conf import settings


class covid19(models.Model):
    country = models.CharField(max_length=250)
    countrycode = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    newconfirmed = models.CharField(max_length=250)
    totalconfirmed = models.CharField(max_length=250)
    newdeaths = models.CharField(max_length=250)
    totaldeaths = models.CharField(max_length=250)
    newrecovered = models.CharField(max_length=250)
    totalrecovered = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'covid19'
        verbose_name_plural = 'covid19s'
