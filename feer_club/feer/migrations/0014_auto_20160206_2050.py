# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 19:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feer', '0013_auto_20160206_1855'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([('beer', 'user')]),
        ),
    ]