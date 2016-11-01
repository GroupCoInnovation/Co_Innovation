# -*- coding:utf-8 -*-
from django.db import models
from SystemArticle.models import Column, Article
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
# Create your models here.

# the same models of SystemArticle
@python_2_unicode_compatible
class Course(models.Model):
    cover = models.ImageField('封面图片', upload_to = 'course/%Y/%m/%d/', default = '/static/base/img/picture/JS.jpg')
    column = models.ForeignKey(Column, verbose_name = '栏目', null = True)
    title = models.CharField('标题', max_length = 100)
    summary = models.TextField('课程摘要', default = '摘要')
    content = models.TextField('课程概述', default = '概述')
    speaker = models.CharField('主讲人', max_length = 100, default = '主讲人')
    time = models.DateTimeField('时间', editable = True, null = True)
    place = models.CharField('地点', max_length = 100, default = '地点')
    like = models.IntegerField('喜欢', default = 0)
    reading_quantity = models.IntegerField('阅读量', default= 0)
    collection = models.IntegerField('收藏', default= 0)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('Course_course', args = [self.id])
    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'
        ordering = ['time']
