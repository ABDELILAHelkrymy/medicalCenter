# Generated by Django 5.1 on 2024-08-29 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_appoitement_isaffected_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoitement',
            name='dateAppoitement',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
