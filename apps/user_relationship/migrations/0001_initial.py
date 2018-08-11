# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-06 21:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import extra_apps.DjangoUeditor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('major', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAchievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_rankings', models.IntegerField(default=0, verbose_name='班级排名')),
                ('monthly_rankings', models.IntegerField(default=0, verbose_name='月排名')),
                ('total_ranking', models.IntegerField(default=0, verbose_name='总排名')),
                ('total_ranking_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='排名时间')),
                ('estimated_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='预计完成时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '学生成绩表',
                'verbose_name_plural': '学生成绩表',
            },
        ),
        migrations.CreateModel(
            name='UserBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(help_text='博客名', max_length=255, verbose_name='博客名')),
                ('blog_body', extra_apps.DjangoUeditor.models.UEditorField(default='', help_text='博客正文', verbose_name='博客正文')),
                ('blog_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '用户博客',
                'verbose_name_plural': '用户博客',
            },
        ),
        migrations.CreateModel(
            name='UserChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_end', models.BooleanField(default=False, help_text='课程是否完成，True或False', verbose_name='课程是否完成')),
                ('chapter_end', models.BooleanField(default=False, help_text='章节是否完成，True或False', verbose_name='章节是否完成')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, help_text='完成时间', verbose_name='完成时间')),
                ('chapter', models.ForeignKey(help_text='章节id', on_delete=django.db.models.deletion.CASCADE, to='major.Chapter', verbose_name='章节名')),
                ('course', models.ForeignKey(help_text='课程id', on_delete=django.db.models.deletion.CASCADE, to='major.Major', verbose_name='课程名')),
                ('user', models.ForeignKey(help_text='用户id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='学生名')),
            ],
            options={
                'verbose_name_plural': '用户章节信息',
                'verbose_name': '用户章节信息',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始学习时间')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='结束时间')),
                ('complete', models.BooleanField(default=False, verbose_name='是否学完')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.Major', verbose_name='课程名')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='学生名')),
            ],
            options={
                'verbose_name': '学生课程',
                'verbose_name_plural': '学生课程',
            },
        ),
        migrations.CreateModel(
            name='UserMajor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开通时间')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='结束时间')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.Major', verbose_name='专业名')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='学生名')),
            ],
            options={
                'verbose_name': '学生专业',
                'verbose_name_plural': '学生专业',
            },
        ),
        migrations.CreateModel(
            name='UserPractice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, help_text='开始时间', verbose_name='开始学习时间')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, help_text='结束时间', verbose_name='结束学习时间')),
                ('practice_info', models.TextField(default='', help_text='练习题提交答案', verbose_name='练习内容')),
                ('count', models.IntegerField(default=0, help_text='练习题提交次数', verbose_name='作业提交次数')),
                ('chapter', models.ForeignKey(help_text='章节id', on_delete=django.db.models.deletion.CASCADE, to='major.Chapter', verbose_name='章节名')),
                ('practice', models.ForeignKey(help_text='练习题id', on_delete=django.db.models.deletion.CASCADE, to='major.Practice', verbose_name='练习名')),
                ('user', models.ForeignKey(help_text='用户id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='学生名')),
            ],
            options={
                'verbose_name_plural': '学生练习信息',
                'verbose_name': '学生练习信息',
            },
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(help_text='作业名字', max_length=255, verbose_name='作业名字')),
                ('download', models.FileField(blank=True, help_text='作业下载地址', null=True, upload_to='', verbose_name='作业下载地址')),
                ('complete_time', models.DateTimeField(default=django.utils.timezone.now, help_text='提交时间', verbose_name='提交时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '学生作业',
                'verbose_name_plural': '学生作业',
            },
        ),
        migrations.AlterUniqueTogether(
            name='userpractice',
            unique_together=set([('user', 'practice')]),
        ),
        migrations.AlterUniqueTogether(
            name='userchapter',
            unique_together=set([('user', 'chapter')]),
        ),
    ]
