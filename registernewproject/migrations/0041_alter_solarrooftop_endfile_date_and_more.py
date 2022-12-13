# Generated by Django 4.0.5 on 2022-08-16 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewproject', '0040_alter_solarrooftop_file_version2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarrooftop',
            name='endFile_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 19, 21, 25, 560736), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='file',
            field=models.FileField(default='-', upload_to='Solar_Rooftop'),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='inputFile_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 16, 19, 21, 25, 560736), max_length=100),
        ),
        migrations.AlterField(
            model_name='tr401',
            name='endFile_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 19, 21, 25, 560736), max_length=100),
        ),
        migrations.AlterField(
            model_name='tr401',
            name='inputFile_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 16, 19, 21, 25, 560736), max_length=100),
        ),
    ]
