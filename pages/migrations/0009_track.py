# Generated by Django 4.0.1 on 2022-02-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_add_trainee_add_trainee1'),
    ]

    operations = [
        migrations.CreateModel(
            name='track',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('track_name', models.CharField(max_length=10)),
            ],
        ),
    ]
