from django.db import models
from datetime import datetime
from django.conf import settings


class covid19(models.Model):
    country = models.CharField(max_length=250)
    countryCode = models.CharField(max_length=250)
    slug = models.CharField(max_length=10)
    newConfirmed = models.IntegerField()
    totalConfirmed = models.IntegerField()
    newDeaths = models.IntegerField()
    totalDeaths = models.IntegerField()
    newRecovered = models.IntegerField()
    totalRecovered = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'covid19'
        verbose_name_plural = 'covid19'
