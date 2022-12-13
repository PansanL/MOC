# Generated by Django 4.0.5 on 2022-09-21 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewproject', '0073_alter_logging_action_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectee',
            name='endFile_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 14, 14, 20, 57, 78292), max_length=100),
        ),
        migrations.AlterField(
            model_name='projectee',
            name='inputFile_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 21, 14, 20, 57, 78292), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='endFile_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 14, 14, 20, 57, 78292), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='inputFile_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
