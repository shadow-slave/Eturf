# Generated by Django 3.2.22 on 2023-11-24 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0006_alter_turf_dbs_taddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turf_dbs',
            name='tetime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='turf_dbs',
            name='tstime',
            field=models.TimeField(),
        ),
    ]
