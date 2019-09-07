#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import re_path
from . import views

app_name = 'TestSummary'
urlpatterns = [
    # debug
    #re_path(r'^home/$', views.lizhiHome),
    re_path(r'^home/$', views.index),
    re_path(r'^add$', views.add),
    re_path(r'^task_queue$', views.task_queue),
    re_path(r'^task_detail$', views.task_detail),
    re_path(r'^diff_detail$', views.diff_detail),
    # url(r'^testcache/task_detail$', TestCache_views.task_detail, name='testcache_task_detail'),
    # url(r'^testcache/set_cancel$', TestCache_views.set_cancel, name='testcache_set_cancel'),
    # url(r'^testcache/re_add$', TestCache_views.re_add, name='testcache_re_add'),
]
