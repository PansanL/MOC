# Generated by Django 4.0.5 on 2022-09-19 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewproject', '0051_alter_projectee_endfile_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectee',
            name='endFile_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 12, 10, 23, 8, 713573), max_length=100),
        ),
        migrations.AlterField(
            model_name='projectee',
            name='inputFile_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 10, 23, 8, 713573), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='endFile_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 12, 10, 23, 8, 712573), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='inputFile_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 19, 10, 23, 8, 712573), max_length=100),
        ),
    ]