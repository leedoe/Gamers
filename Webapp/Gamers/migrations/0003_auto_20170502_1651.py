# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gamers', '0002_auto_20170430_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='homepage',
            field=models.URLField(null=True),
        ),
    ]
