# Generated by Django 4.0.5 on 2022-07-01 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewproject', '0005_alter_registernewproject_folderstructure_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registernewproject',
            name='folderstructure_image',
            field=models.ImageField(blank=True, upload_to='sub_image'),
        ),
    ]
