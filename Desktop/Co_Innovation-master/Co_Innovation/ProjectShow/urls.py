#-*- coding:utf-8 -*-
from django.conf.urls import url, include
from ProjectShow.views import *
urlpatterns = [
    url(r'^index$', 'ProjectShow.views.index', name = 'ProjectShow_index'),
    url('^project/(?P<project_id>[0-9]+)/$', 'ProjectShow.views.project_detail', name = 'project_detail'),
    url('^change_project_name_and_intro/(?P<project_id>[0-9]+)/$', change_project_name_and_intro, name='change_project_name_and_intro'),
    url('^end_project/(?P<project_id>[0-9]+)/$', end_project, name='end_project'),
    url(r'^project_manage$', 'ProjectShow.views.project_manage', name = 'project_manage'),
    url(r'^add_member/(?P<project_id>[0-9]+)/$', 'ProjectShow.views.add_member', name='add_member'),
    url(r'^add_task/(?P<project_id>[0-9]+)/$', 'ProjectShow.views.add_task', name='add_task'),
    url(r'^change_role/$', 'ProjectShow.views.change_role', name='change_role'),
    # url(r'')
]
