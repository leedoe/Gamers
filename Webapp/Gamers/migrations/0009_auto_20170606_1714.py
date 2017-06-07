# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-06 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gamers', '0008_auto_20170527_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='steam_id',
        ),
        migrations.AddField(
            model_name='game',
            name='authen',
            field=models.BooleanField(default=False),
        ),
    ]
