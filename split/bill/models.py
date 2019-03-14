from django.db import models
import datetime


class Bill(models.Model):
    name_bill = models.CharField(max_length=255)
    amount = models.FloatField()
    description = models.CharField(max_length=2083)
    date_bill = models.DateTimeField(default=datetime.datetime.now, blank=True)


class Share(models.Model):
    name_shared = models.CharField(max_length=255)
    amount_shared = models.FloatField()



