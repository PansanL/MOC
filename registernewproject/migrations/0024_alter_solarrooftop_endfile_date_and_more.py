# Generated by Django 4.0.5 on 2022-07-27 08:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewproject', '0023_alter_solarrooftop_endfile_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarrooftop',
            name='endFile_date',
            field=models.CharField(default=datetime.datetime(2022, 8, 26, 8, 30, 12, 270428), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='inputFile_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 8, 30, 12, 270428), max_length=100),
        ),
    ]
