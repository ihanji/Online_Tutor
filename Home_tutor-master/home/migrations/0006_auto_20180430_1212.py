# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180420_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionbase',
            old_name='category',
            new_name='subject',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subject',
            field=models.IntegerField(default=-1),
        ),
    ]
