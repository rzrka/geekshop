# Generated by Django 2.2.16 on 2020-11-21 00:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0007_auto_20201118_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 23, 0, 4, 40, 383958, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
