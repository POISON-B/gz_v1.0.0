# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-25 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0003_remove_image_chaptertask_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='ChapterTask_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='major.ChapterTask', verbose_name='任务'),
            preserve_default=False,
        ),
    ]
