# Generated by Django 5.1 on 2024-08-29 19:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_appoitement_dateappoitement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appoitement',
            name='isAffected',
        ),
        migrations.AddField(
            model_name='appoitement',
            name='dateAppoitement',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
