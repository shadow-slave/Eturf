# Generated by Django 3.2.22 on 2023-11-20 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turf_dbs',
            name='features2',
        ),
        migrations.AlterField(
            model_name='turf_dbs',
            name='features',
            field=models.CharField(default='', max_length=25),
        ),
    ]