# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-14 02:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.manager
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190313_1859'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='useractivation',
            managers=[
                ('pending', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='useractivation',
            name='date_created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 3, 14, 2, 21, 22, 503906, tzinfo=utc)),
        ),
    ]