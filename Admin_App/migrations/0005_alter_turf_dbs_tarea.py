# Generated by Django 3.2.22 on 2023-11-23 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0004_alter_turf_dbs_taddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turf_dbs',
            name='tarea',
            field=models.CharField(max_length=100),
        ),
    ]
