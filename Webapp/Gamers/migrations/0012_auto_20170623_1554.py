# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 06:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gamers', '0011_auto_20170623_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='Tags',
            new_name='tags',
        ),
    ]
