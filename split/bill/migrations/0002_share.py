# Generated by Django 2.1.7 on 2019-03-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_shared', models.CharField(max_length=255)),
                ('amount_shared', models.FloatField()),
            ],
        ),
    ]