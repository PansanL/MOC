# Generated by Django 4.0.5 on 2022-07-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewproject', '0002_alter_registernewproject_end_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registernewproject',
            name='start_project',
            field=models.DateTimeField(),
        ),
    ]
