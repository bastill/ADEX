# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-13 14:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='UserActivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone_num', models.CharField(max_length=13)),
                ('t_and_c', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=30)),
                ('password_2', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(verbose_name=datetime.datetime(2019, 3, 13, 14, 28, 33, 299274, tzinfo=utc))),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.UserActivation'),
        ),
    ]