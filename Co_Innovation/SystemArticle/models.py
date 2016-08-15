#-*- coding:utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
import django.utils.timezone
from User.models import User
# Create your models here.
@python_2_unicode_compatible
class Column(models.Model):
    shirt_category_choices = (
        ('SC', '系统文章栏目'),
        ('CC', '课程文章栏目'),
    )
    category = models.CharField('栏目类别', choices = shirt_category_choices, max_length = 20, default = 'SC')
    column_name = models.CharField('栏目名称', max_length = 250)
    column_text = models.CharField('栏目简介', max_length = 250, blank = True)
    def __str__(self):
        return  self.column_name
    def __unicode__(self):
        return self.column_name
    def get_absolute_url(self):
        return reverse('SystemArticle_column', args = [self.id])
    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['category','column_name']

@python_2_unicode_compatible
class Article(models.Model):
    shirt_category_choices = (
        ('SA', '系统文章'),
        ('CA', '课程文章'),
    )
    cover = models.ImageField('封面图片', upload_to = './article/%Y/%m/%d/', max_length = 100, default = '/static/base/img/picture/pageR.png', blank = True, null = True)
    category = models.CharField('文章类别', choices = shirt_category_choices, max_length = 20, default = 'SA')
    column = models.ForeignKey(Column, verbose_name = '栏目', default = True)
    title = models.CharField('标题', max_length = 100)
    summary = models.TextField('摘要', default = '摘要', null = True, blank = True)
    pub_user = models.ForeignKey(User, verbose_name = '发布者', null = True, blank = True)
    author = models.CharField('文章作者', max_length = 50, default = None, blank = True, null = True)
    pub_date = models.DateTimeField('发布时间', auto_now_add = True, editable = True)
    update_time = models.DateTimeField('更新时间', auto_now = True)
    content = models.TextField('内容')
    reading_quantity = models.IntegerField('阅读量', default = 0, blank = True)
    collection = models.ManyToManyField(User, related_name = 'article_collection', default = True, blank = True)
    top = models.BooleanField('置顶', default = False, blank = True)
    top_time = models.DateTimeField('置顶时间',editable = True) # for thr ordering of the top items
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('SystemArticle_article', args = [self.id])
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['category','-top', '-top_time','pub_date']
