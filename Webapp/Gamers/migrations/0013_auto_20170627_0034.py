# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-26 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gamers', '0012_auto_20170623_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
