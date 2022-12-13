# Generated by Django 4.0.5 on 2022-08-08 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewproject', '0038_solarrooftop_file_version1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solarrooftop',
            name='File_Version1',
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='endFile_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 1, 13, 20, 46, 20028), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='inputFile_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 8, 13, 20, 46, 20028), max_length=100),
        ),
        migrations.AlterField(
            model_name='tr401',
            name='endFile_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 1, 13, 20, 46, 20028), max_length=100),
        ),
        migrations.AlterField(
            model_name='tr401',
            name='inputFile_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 8, 13, 20, 46, 20028), max_length=100),
        ),
    ]