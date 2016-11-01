#-*- coding:utf-8 -*-

from django.conf.urls import include, url
from upload_proc import simditor_file_upload


urlpatterns = [
    url(r'^index$', 'SystemArticle.views.index', name = 'SystemArticle_index'),
    url(r'^column/(?P<column_id>[0-9]+)/$', 'SystemArticle.views.column', name = 'SystemArticle_column'),
    url(r'^article/(?P<article_id>[0-9]+)/$', 'SystemArticle.views.article', name = 'SystemArticle_article'),
    url(r'^write_article$', 'SystemArticle.views.write_article', name = 'SystemArticle_write_article'),
    url(r'^top/(?P<article_id>[0-9]+)/$', 'SystemArticle.views.top', name = 'top'),
    url(r'^untop/(?P<article_id>[0-9]+)/$', 'SystemArticle.views.untop', name = 'untop'),
    url(r'^edit_article/(?P<article_id>[0-9]+)/$', 'SystemArticle.views.edit_article', name = 'SystemArticle_edit_article'),
    url(r'^delete_article/(?P<article_id>[0-9]+)/$', 'SystemArticle.views.delete_article', name = 'delete_article'),
    url(r'^upload$', simditor_file_upload, name = 'simditor_file_upload'),
    url(r'^preview$', 'SystemArticle.views.preview', name='SystemArticle_preview'),
    url(r'^show_upload_file$', 'SystemArticle.views.show_upload_file', name='SystemArticle_show_upload_file'),
    url(r'^upload_file$', 'SystemArticle.views.upload_file', name='SystemArticle_upload_file'),
]
