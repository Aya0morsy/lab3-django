# Generated by Django 4.0.1 on 2022-02-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_myuser1_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_trainee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trainee_name', models.CharField(max_length=10)),
                ('faculty', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='add_trainee1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trainee_name', models.CharField(max_length=10)),
                ('faculty', models.CharField(max_length=16)),
            ],
        ),
    ]
