# Generated by Django 4.0.6 on 2022-11-08 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewproject', '0081_smartchecksheetsubone_delete_smartchecksheet_sub1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlfaultdetection',
            name='endFile_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 1, 14, 49, 18, 263893), max_length=100),
        ),
        migrations.AlterField(
            model_name='projectee',
            name='endFile_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 1, 14, 49, 18, 263893), max_length=100),
        ),
        migrations.AlterField(
            model_name='smartchecksheetsubone',
            name='endFile_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 1, 14, 49, 18, 263893), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='endFile_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 1, 14, 49, 18, 263893)),
        ),
    ]