# Generated by Django 2.1.7 on 2019-03-07 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_bill', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('description', models.CharField(max_length=2083)),
                ('date_bill', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
