# -*- coding:utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from User.models import User
import hashlib
from django.core.urlresolvers import reverse

# Create your models here.
@python_2_unicode_compatible
class Project(models.Model):
    shirt_status_choices = (
        (0, '未完成'),
        (1, '已完成未发表'),
        (2, '完成并发表'),
    )
    cover = models.ImageField('封面图片',upload_to = './project/', max_length = 100, default = '/static/base/img/index/new-class.jpg')
    project_name = models.CharField('项目名称', max_length = 100, default = '项目文章')
    project_intro = models.TextField('项目概述', default = '项目概述')
    principal = models.ForeignKey(User, related_name = 'principal_project_set', verbose_name = '负责人')
    members = models.ManyToManyField(User, related_name = 'member_project_set', verbose_name = '成员')
    status = models.IntegerField('状态', default = 0, choices = shirt_status_choices)
    start_time = models.DateTimeField('开始时间',auto_now_add = True,editable = True)
    deadline = models.DateTimeField('截止时间', auto_now = True, null = True)
    collection = models.ManyToManyField(User, verbose_name = '收藏', related_name = 'project_collection', default = True, blank = True)
    reading_quantity = models.IntegerField('阅读量', default= 0, blank = True)
    def __str__(self):
        return self.project_name
    def get_absolute_url(self):
        return reverse('project_detail', args = [self.id])
    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'
        ordering = ['status', 'project_name']

@python_2_unicode_compatible
class Task(models.Model):
    task_name = models.CharField('任务名称', max_length = 100, default = '任务')
    project = models.ForeignKey(Project, verbose_name = '对应项目', null = True)
    worker = models.ForeignKey(User, verbose_name = '工作者', null = True)
    reward = models.IntegerField('金币', default = 0)
    is_finished = models.BooleanField('是否完成', default = False)
    finish_time = models.DateTimeField('完成时间',null = True)
    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = '任务'
        ordering = ['is_finished', 'project']
