# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 17:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feer', '0003_auto_20160114_1836'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderList',
            new_name='Order',
        ),
    ]