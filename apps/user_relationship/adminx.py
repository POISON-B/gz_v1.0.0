#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-4 上午10:28
# @Author  : Shark
# @File    : adminx.py
# @Software: PyCharm

from extra_apps import xadmin

from apps.user_relationship.models import *


class UserMajorAdmin(object):
    list_display = ['user', 'major', 'create_time', 'end_time']
    search_fields = ['user', 'major']
    list_filter = ['user', 'major', 'create_time', 'end_time']
    readonly_fields = ['user', 'major', 'create_time', 'end_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'start_time', 'end_time', 'complete']
    search_fields = ['user', 'course', 'complete']
    list_filter = ['user', 'course', 'start_time', 'end_time', 'complete']
    readonly_fields = ['user', 'course', 'start_time', 'end_time', 'complete']


class UserChapterAdmin(object):
    list_display = ['user', 'chapter', 'course', 'course_end', 'chapter_end', 'end_time']
    search_fields = ['user', 'chapter', 'course', 'course_end', 'chapter_end']
    list_filter = ['user', 'chapter', 'course', 'course_end', 'chapter_end', 'end_time']
    readonly_fields = ['user', 'chapter', 'course', 'course_end', 'chapter_end', 'end_time']


class UserPracticeAdmin(object):
    list_display = ['user', 'chapter', 'practice', 'start_time', 'end_time', 'practice_info', 'count']
    search_fields = ['user', 'chapter', 'practice', 'practice_info', 'count']
    list_filter = ['user', 'chapter', 'practice', 'start_time', 'end_time', 'practice_info', 'count']
    readonly_fields = ['user', 'chapter', 'practice', 'start_time', 'end_time', 'practice_info', 'count']


class UserAchievementAdmin(object):
    list_display = ['user', 'class_rankings', 'monthly_rankings', 'total_ranking', 'estimated_time', 'hesternal']
    search_fields = ['user', 'estimated_time', 'hesternal']
    list_filter = ['user', 'estimated_time', 'hesternal']
    readonly_fields = ('user', 'class_rankings', 'monthly_rankings', 'total_ranking', 'estimated_time', 'hesternal', 'total_ranking_time')


class UserTaskAdmin(object):
    list_display = ['user', 'task_name', 'complete_time', 'task_info']
    search_fields = ['user', 'task_name']
    list_filter = ['user', 'task_name', 'complete_time', 'task_info']
    readonly_filter = ('user', 'task_name', 'complete_time', 'task_info')


class UserBlogAdmin(object):
    list_display = ['user', 'blog_name', 'blog_body', 'blog_time']
    search_fields = ['user', 'blog_name', 'blog_body']
    list_filter = ['user', 'blog_name', 'blog_body', 'blog_time']
    readonly_filter = ['user', 'blog_name', 'blog_body', 'blog_time']


xadmin.site.register(UserMajor, UserMajorAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserChapter, UserChapterAdmin)
xadmin.site.register(UserPractice, UserPracticeAdmin)
xadmin.site.register(UserAchievement, UserAchievementAdmin)
xadmin.site.register(UserTask, UserTaskAdmin)
xadmin.site.register(UserBlog, UserBlogAdmin)
