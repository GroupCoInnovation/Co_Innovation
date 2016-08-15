#-*- coding:utf-8 -*-
from django.contrib import admin
from SystemArticle.models import Column, Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'pub_date', 'update_time')
    list_filter = ['category','pub_date', 'column']
    search_fields = ['column', 'title']
    fieldsets = [
        (None, {'fields':['cover', 'column', 'title', 'pub_user', 'author']}),
        ('摘要', {'fields':['summary'], 'classes':['collapse']}),
        ('time', {'fields':['top_time'], 'classes':['collapse']}),
        ('content', {'fields':['content', 'reading_quantity', 'collection','top']}),
    ]

class ColumnAdmin(admin.ModelAdmin):
    list_display = ('category', 'column_name')
    list_filter = ['category']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Column, ColumnAdmin)
