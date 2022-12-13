# Generated by Django 4.0.5 on 2022-07-21 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewproject', '0021_solarrooftop_retention'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solarrooftop',
            name='retention',
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='endFile_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='inputFile_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarrooftop',
            name='status',
            field=models.CharField(default='-', max_length=20, null=True),
        ),
    ]
