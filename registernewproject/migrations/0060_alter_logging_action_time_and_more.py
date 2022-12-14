# Generated by Django 4.0.5 on 2022-09-20 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewproject', '0059_alter_logging_action_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logging',
            name='Action_Time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='projectee',
            name='endFile_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 13, 15, 50, 48, 704145), max_length=100),
        ),
        migrations.AlterField(
            model_name='projectee',
            name='inputFile_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 20, 15, 50, 48, 704145), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='endFile_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 13, 15, 50, 48, 704145), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='inputFile_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 20, 15, 50, 48, 704145), max_length=100),
        ),
    ]
