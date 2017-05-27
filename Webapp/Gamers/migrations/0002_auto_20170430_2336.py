# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gamers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='pictures',
        ),
        migrations.AddField(
            model_name='picture',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gamers.Game'),
        ),
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]