from django.db import models


class Dataset(models.Model):
    date = models.DateField()
    channel = models.CharField(max_length=150)
    country = models.CharField(max_length=2)
    os = models.CharField(max_length=150)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.DecimalField(max_digits=9, decimal_places=2)
    revenue = models.DecimalField(max_digits=9, decimal_places=2)
