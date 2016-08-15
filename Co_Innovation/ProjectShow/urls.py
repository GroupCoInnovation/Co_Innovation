#-*- coding:utf-8 -*-
from django.conf.urls import url, include

urlpatterns = [
    url(r'^index$', 'ProjectShow.views.index', name = 'ProjectShow_index'),
    url('^project/(?P<project_id>[0-9]+)/$', 'ProjectShow.views.project_detail', name = 'project_detail'),
    url(r'^project_manage$', 'ProjectShow.views.project_manage', name = 'project_manage'),
    # url(r'')
]
