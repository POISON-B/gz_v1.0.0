# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-26 10:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arena', '0005_auto_20180825_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpass',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 26, 10, 40, 24, 980497), verbose_name='用户提交时间'),
        ),
    ]
