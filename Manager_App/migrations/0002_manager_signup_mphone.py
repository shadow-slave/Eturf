# Generated by Django 3.2.22 on 2023-11-28 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager_signup',
            name='mphone',
            field=models.IntegerField(default=0),
        ),
    ]
