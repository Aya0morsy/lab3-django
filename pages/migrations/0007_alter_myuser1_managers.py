# Generated by Django 4.0.1 on 2022-02-06 12:06

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_myuser1'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='myuser1',
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
