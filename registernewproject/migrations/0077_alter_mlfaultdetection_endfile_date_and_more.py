# Generated by Django 4.0.6 on 2022-09-27 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewproject', '0076_mlfaultdetection_alter_projectee_endfile_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlfaultdetection',
            name='endFile_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 20, 9, 44, 8, 107257), max_length=100),
        ),
        migrations.AlterField(
            model_name='projectee',
            name='endFile_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 20, 9, 44, 8, 107257), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='endFile_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 20, 9, 44, 8, 107257)),
        ),
    ]
