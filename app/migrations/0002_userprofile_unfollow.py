# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='unfollow',
            field=models.ManyToManyField(to='app.UserProfile'),
        ),
    ]
