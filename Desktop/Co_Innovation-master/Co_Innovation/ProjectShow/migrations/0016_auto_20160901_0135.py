# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectShow', '0015_auto_20160815_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='role',
            field=models.CharField(default=b'\xe8\x81\x8c\xe5\x8a\xa1', max_length=100, verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_time',
            field=models.DateField(auto_now_add=True, verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='task',
            name='worker',
            field=models.ForeignKey(related_name='worker', verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe8\x80\x85', to='User.User', null=True),
        ),
    ]
