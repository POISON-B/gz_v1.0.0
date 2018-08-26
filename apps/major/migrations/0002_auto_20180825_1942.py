# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-25 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='截图名')),
                ('image', models.ImageField(blank=True, null=True, upload_to='task/images/', verbose_name='任务截图')),
                ('add_time', models.DateTimeField(blank=True, null=True, verbose_name='上传时间')),
            ],
            options={
                'verbose_name': '任务截图',
                'verbose_name_plural': '任务截图',
            },
        ),
        migrations.RemoveField(
            model_name='chaptertask',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='ChapterTask_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.ChapterTask', verbose_name='任务'),
        ),
    ]