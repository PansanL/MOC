# Generated by Django 4.0.5 on 2022-09-21 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewproject', '0075_alter_projectee_endfile_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MLFAULTDETECTION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=255, null=True)),
                ('inputFile_date', models.DateTimeField(auto_now_add=True)),
                ('endFile_date', models.DateField(default=datetime.datetime(2023, 9, 14, 14, 32, 50, 899488), max_length=100)),
                ('status', models.CharField(default='-', max_length=20, null=True)),
                ('file', models.FileField(default='-', upload_to='ML_FaultDetection')),
                ('File_Version2', models.FileField(default='-', null=True, upload_to='ML_FaultDetection/File_version2')),
                ('File_Version3', models.FileField(default='-', null=True, upload_to='ML_FaultDetection/File_version3')),
                ('File_Version4', models.FileField(default='-', null=True, upload_to='ML_FaultDetection/File_version4')),
                ('File_Version5', models.FileField(default='-', null=True, upload_to='ML_FaultDetection/File_version5')),
            ],
        ),
        migrations.AlterField(
            model_name='projectee',
            name='endFile_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 14, 14, 32, 50, 898488), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='endFile_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 14, 14, 32, 50, 898488)),
        ),
    ]
