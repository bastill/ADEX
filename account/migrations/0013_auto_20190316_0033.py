# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-16 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20190315_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='status',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=14),
        ),
    ]
