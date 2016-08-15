# -*- coding:utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import hashlib
# Create your models here.
def encry_password(password):
    p = hashlib.md5()
    p.update(password)
    return p.hexdigest()

@python_2_unicode_compatible
class User(models.Model):
    head_image = models.ImageField('头像', upload_to = './user/%Y/%m/%d/', max_length = 100, default = '/static/base/img/index/Avatar.png', blank = True, null = True)
    user_name = models.CharField('用户名', max_length = 100)
    password = models.CharField('密码', max_length = 100, default = encry_password('123456'))
    # bit: (编辑权限)(开用户)(置顶)(编辑文章)(写文章)(超级用户) 000000
    root = models.IntegerField('权限', default = 0)
    email = models.EmailField('邮箱', blank = True)
    major = models.CharField('专业', max_length = 100, blank = True)
    def __unicode__(self):
        return self.user_name
    def __str__(self):
        return self.user_name
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
        ordering = ['-root', 'user_name']
