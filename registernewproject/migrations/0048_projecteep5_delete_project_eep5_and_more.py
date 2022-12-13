# Generated by Django 4.0.5 on 2022-08-27 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewproject', '0047_alter_project_eep5_endfile_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PROJECTEEP5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=38, null=True)),
                ('tags', models.CharField(max_length=38, null=True)),
                ('inputFile_date', models.DateTimeField(default=datetime.datetime(2022, 8, 27, 15, 3, 14, 735944), max_length=100)),
                ('endFile_date', models.DateTimeField(default=datetime.datetime(2023, 8, 20, 15, 3, 14, 735944), max_length=100)),
                ('status', models.CharField(default='-', max_length=20, null=True)),
                ('file', models.FileField(default='-', upload_to='PROJECT_EEP5')),
                ('File_Version2', models.FileField(default='-', null=True, upload_to='PROJECT_EEP5/File_version2')),
                ('File_Version3', models.FileField(default='-', null=True, upload_to='PROJECT_EEP5/File_version3')),
                ('File_Version4', models.FileField(default='-', null=True, upload_to='PROJECT_EEP5/File_version4')),
                ('File_Version5', models.FileField(default='-', null=True, upload_to='PROJECT_EEP5/File_version5')),
            ],
        ),
        migrations.DeleteModel(
            name='PROJECT_EEP5',
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='endFile_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 20, 15, 3, 14, 735944), max_length=100),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='inputFile_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 15, 3, 14, 735944), max_length=100),
        ),
    ]