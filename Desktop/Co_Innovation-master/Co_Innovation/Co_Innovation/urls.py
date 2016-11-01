#-*- coding:utf-8 -*-
"""Co_Innovation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
import django

urlpatterns = [
    # accept a queryset argument root_process_url /root_process/?option_url_name=...
    # url(r'^root_process/$', 'home.views.root_process', name = 'root_process'),
    url(r'^$', 'home.views.home', name = 'home'),
    url(r'^fuzzy_search$', 'home.views.fuzzy_search', name = 'fuzzy_search'),
    url(r'^personal_homepage$', 'home.views.personal_homepage', name = 'personal_homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^User/', include('User.urls')),
    #url(r'^home/', include('home.urls')),
    url(r'^Course/', include('Course.urls')),
    url(r'^ProjectShow/', include('ProjectShow.urls')),
    url(r'^SystemArticle/', include('SystemArticle.urls')),
    url(r'^uploads/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
]
