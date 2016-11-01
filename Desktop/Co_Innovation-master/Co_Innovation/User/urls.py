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
#from django.contrib import admin

urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
    # url(r'^(?P<user_id>[0-9]+)&(?P<password>\w+)$', 'User.views.home_user', name = 'home_user'),
    url(r'^register$', 'User.views.register', name = 'register'),
    url(r'^login$', 'User.views.login', name = 'login'),
    url(r'^log_out$', 'User.views.log_out', name = 'log_out'),
    url(r'^edit_root$', 'User.views.edit_root', name = 'edit_root'),
    url(r'^edit_root_process$', 'User.views.edit_root_process', name = 'edit_root_process'),
    url(r'^find$', 'User.views.find', name = 'find_user'),
]
