from django.db import models
from datetime import datetime
from django.conf import settings


class covid19(models.Model):
    Country = models.CharField(max_length=250)
    CountryCode = models.CharField(max_length=250)
    Slug = models.CharField(max_length=10)
    NewConfirmed = models.IntegerField()
    TotalConfirmed = models.IntegerField()
    NewDeaths = models.IntegerField()
    TotalDeaths = models.IntegerField()
    NewRecovered = models.IntegerField()
    TotalRecovered = models.IntegerField()
    Date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'covid19'
        verbose_name_plural = 'covid19'
