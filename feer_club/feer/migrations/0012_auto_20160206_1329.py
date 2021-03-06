# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 12:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feer', '0011_auto_20160206_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='reviews',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='profile',
        ),
        migrations.AddField(
            model_name='beer',
            name='ratings',
            field=models.ManyToManyField(through='feer.Rating', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
