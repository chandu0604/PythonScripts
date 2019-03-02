from django.db import models
import datetime


class Bill(models.Model):
    name_bill = models.CharField(max_length=255)
    amount = models.FloatField()
    description = models.CharField(max_length=2083)
    date_bill = models.DateTimeField(default=datetime.date.today)

