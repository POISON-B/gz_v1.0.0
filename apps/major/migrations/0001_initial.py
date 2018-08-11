# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-06 21:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import extra_apps.DjangoUeditor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(help_text='章节名字', max_length=255, verbose_name='章节名字')),
                ('chapter_number', models.IntegerField(verbose_name='章节数')),
                ('chapter_introduce', models.CharField(max_length=255, verbose_name='章节介绍')),
                ('chapter_video', models.CharField(blank=True, max_length=255, null=True, verbose_name='视频')),
                ('chapter_task', extra_apps.DjangoUeditor.models.UEditorField(default='', verbose_name='章节任务说明')),
                ('chapter_target', models.CharField(max_length=255, verbose_name='章节目标')),
            ],
            options={
                'verbose_name': '章节',
                'verbose_name_plural': '章节',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名')),
                ('category_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], help_text='类目级别', verbose_name='类目级别')),
                ('course_task', models.CharField(blank=True, max_length=255, null=True, verbose_name='内容介绍')),
                ('image', models.ImageField(blank=True, null=True, upload_to='course/images/', verbose_name='封面图')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('parent_category', models.ForeignKey(blank=True, default='self', help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='major.Major', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '专业类别',
                'verbose_name_plural': '专业类别',
            },
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_name', models.CharField(help_text='练习id', max_length=255, verbose_name='练习名')),
                ('Practice_standard', models.CharField(help_text='练习过关标准信息', max_length=255, verbose_name='过关标准')),
                ('standard_explain', models.CharField(help_text='练习说明', max_length=255, verbose_name='题目说明')),
                ('standard_answer', models.CharField(help_text='练习答案', max_length=255, verbose_name='练习答案')),
                ('chapter_name', models.ForeignKey(help_text='章节id', on_delete=django.db.models.deletion.CASCADE, to='major.Chapter', verbose_name='章节')),
            ],
            options={
                'verbose_name': '练习',
                'verbose_name_plural': '练习',
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.Major', verbose_name='课程'),
        ),
        migrations.AlterUniqueTogether(
            name='chapter',
            unique_together=set([('course_name', 'chapter_number')]),
        ),
    ]
