# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-14 02:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20190313_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivation',
            name='date_created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 3, 14, 2, 24, 19, 106677, tzinfo=utc)),
        ),
    ]
