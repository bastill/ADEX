# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-14 17:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='date_created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 3, 14, 17, 54, 52, 576359, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='description',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='task_title',
            field=models.CharField(max_length=100),
        ),
    ]
