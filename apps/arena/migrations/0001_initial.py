# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-22 22:38
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('major', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pk_mode', models.IntegerField(choices=[(1, '时间赛'), (2, '速度赛'), (3, '编程赛')], default=1, verbose_name='挑战类别')),
                ('status', models.CharField(max_length=10, verbose_name='挑战状态')),
                ('be_challenged', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='be_chg', to=settings.AUTH_USER_MODEL, verbose_name='被挑战者')),
                ('challenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chg', to=settings.AUTH_USER_MODEL, verbose_name='挑战者')),
            ],
            options={
                'verbose_name': '挑战者表',
                'verbose_name_plural': '挑战者表',
            },
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='关卡名称')),
                ('pass_no', models.CharField(max_length=20, verbose_name='关卡编号')),
                ('pass_intr', models.CharField(max_length=500, verbose_name='关卡说明')),
                ('pass_std', models.CharField(max_length=600, verbose_name='过关标准')),
                ('pass_answer', models.CharField(max_length=800, verbose_name='关卡答案')),
                ('pass_limit_time', models.CharField(max_length=20, verbose_name='限时时间')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.Major', verbose_name='专业信息')),
            ],
            options={
                'verbose_name': '单个关卡',
                'verbose_name_plural': '单个关卡',
            },
        ),
        migrations.CreateModel(
            name='PkQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='题目名称')),
                ('content', models.CharField(max_length=500, verbose_name='题目内容')),
                ('answer', models.CharField(max_length=500, verbose_name='题目答案')),
                ('complete_time', models.CharField(max_length=30, verbose_name='完成时间')),
            ],
            options={
                'verbose_name': 'pk题目',
                'verbose_name_plural': 'pk题目',
            },
        ),
        migrations.CreateModel(
            name='TeamComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='团赛题目')),
                ('content', models.CharField(max_length=500, verbose_name='团赛内容')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('member_num', models.IntegerField(verbose_name='成员数量')),
                ('recruit', models.CharField(max_length=500, verbose_name='征召说明')),
            ],
            options={
                'verbose_name': '团赛',
                'verbose_name_plural': '团赛',
            },
        ),
        migrations.CreateModel(
            name='UserPass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_score', models.IntegerField(default=0, verbose_name='关卡评分')),
                ('user_submit', models.CharField(max_length=2000, verbose_name='用户提交代码')),
                ('submit_time', models.DateTimeField(default=datetime.datetime(2018, 8, 22, 22, 38, 34, 97917), verbose_name='用户提交时间')),
                ('complete_time', models.IntegerField(default=0, verbose_name='完成用时')),
                ('submit_num', models.IntegerField(default=0, verbose_name='用户提交次数')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='学生名')),
                ('user_pass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arena.Pass', verbose_name='关卡')),
            ],
            options={
                'verbose_name': '用户关卡表',
                'verbose_name_plural': '用户关卡表',
            },
        ),
        migrations.CreateModel(
            name='UserPkDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_comp_status', models.IntegerField(default=0, verbose_name='用户完成题数')),
                ('challenger_comp_status', models.IntegerField(default=0, verbose_name='挑战者完成题数')),
                ('user_score', models.IntegerField(default=0, verbose_name='用户得分')),
                ('chalenger_score', models.IntegerField(default=0, verbose_name='挑战者得分')),
                ('challenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arena.Challenger', verbose_name='挑战者信息')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户信息')),
            ],
            options={
                'verbose_name': 'pk详情表',
                'verbose_name_plural': 'pk详情表',
            },
        ),
        migrations.CreateModel(
            name='UserPkExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answer', models.CharField(max_length=500, verbose_name='用户答案')),
                ('challenger_answer', models.CharField(max_length=500, verbose_name='挑战者答案')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arena.PkQuestion', verbose_name='pk题目')),
                ('user_pk_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arena.UserPkDetail', verbose_name='当前用户pk详情')),
            ],
            options={
                'verbose_name': '用户pk题目',
                'verbose_name_plural': '用户pk题目',
            },
        ),
        migrations.CreateModel(
            name='UserTeamComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, verbose_name='用户id')),
                ('join_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='加入时间')),
                ('duty', models.CharField(max_length=50, verbose_name='担任岗位')),
                ('team_comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arena.TeamComp', verbose_name='参与团赛')),
            ],
            options={
                'verbose_name': '用户团赛信息',
                'verbose_name_plural': '用户团赛信息',
            },
        ),
    ]
