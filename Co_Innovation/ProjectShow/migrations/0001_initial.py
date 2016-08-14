# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_auto_20160806_0700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(default=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x96\x87\xe7\xab\xa0', max_length=100, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('project_intro', models.TextField(default=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\xa6\x82\xe8\xbf\xb0', verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\xa6\x82\xe8\xbf\xb0')),
                ('status', models.IntegerField(default=0, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('start_time', models.DateTimeField(verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('deadline', models.DateTimeField(verbose_name=b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xb6\xe9\x97\xb4')),
                ('principal', models.ForeignKey(verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba', to='User.User')),
            ],
            options={
                'verbose_name': '\u9879\u76ee',
                'verbose_name_plural': '\u9879\u76ee',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_name', models.CharField(max_length=100, verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe5\x90\x8d\xe7\xa7\xb0')),
                ('reward', models.IntegerField(default=0, verbose_name=b'\xe9\x87\x91\xe5\xb8\x81')),
                ('is_finished', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xae\x8c\xe6\x88\x90')),
                ('finish_time', models.DateTimeField(verbose_name=b'\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xb6\xe9\x97\xb4')),
                ('project', models.ForeignKey(verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe9\xa1\xb9\xe7\x9b\xae', to='ProjectShow.Project')),
                ('worker', models.ForeignKey(verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe8\x80\x85', to='User.User')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1',
                'verbose_name_plural': '\u4efb\u52a1',
            },
        ),
    ]
