# Generated by Django 3.2.22 on 2023-11-23 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0003_alter_turf_dbs_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turf_dbs',
            name='taddress',
            field=models.URLField(),
        ),
    ]
