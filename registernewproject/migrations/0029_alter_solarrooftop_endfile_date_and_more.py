# Generated by Django 4.0.5 on 2022-07-28 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewproject', '0028_alter_solarrooftop_endfile_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarrooftop',
            name='endFile_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 13, 5, 17, 879791), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='file_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='inputFile_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 28, 13, 5, 17, 879791), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='tags',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='tr401',
            name='endFile_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 13, 5, 17, 879791), max_length=100),
        ),
        migrations.AlterField(
            model_name='tr401',
            name='file_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tr401',
            name='inputFile_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 28, 13, 5, 17, 879791), max_length=100),
        ),
        migrations.AlterField(
            model_name='tr401',
            name='tags',
            field=models.CharField(max_length=35, null=True),
        ),
    ]
