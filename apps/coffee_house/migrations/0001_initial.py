# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-23 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscussMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('content', models.CharField(max_length=2000, verbose_name='内容')),
                ('send_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发送时间')),
                ('click_num', models.IntegerField(default=0, verbose_name='浏览数')),
            ],
            options={
                'verbose_name': '论坛信息',
                'verbose_name_plural': '论坛信息',
            },
        ),
        migrations.CreateModel(
            name='DiscussReplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发送时间')),
                ('content', models.CharField(max_length=2000, verbose_name='回复内容')),
            ],
            options={
                'verbose_name': '论坛信息回复',
                'verbose_name_plural': '论坛信息回复',
            },
        ),
        migrations.CreateModel(
            name='StudentMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000, verbose_name='发送的消息')),
                ('send_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发送时间')),
                ('msg_status', models.IntegerField(choices=[(0, '未读'), (1, '已读')], default=0, verbose_name='消息状态')),
            ],
            options={
                'verbose_name': '学生消息',
                'verbose_name_plural': '学生消息',
            },
        ),
        migrations.CreateModel(
            name='TeacherUserMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000, verbose_name='发送的消息')),
                ('send_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发送时间')),
                ('msg_type', models.IntegerField(choices=[(0, '学生消息'), (1, '讲师消息')], default=0, verbose_name='消息类型')),
            ],
            options={
                'verbose_name': '老师学生消息',
                'verbose_name_plural': '老师学生消息',
            },
        ),
    ]
