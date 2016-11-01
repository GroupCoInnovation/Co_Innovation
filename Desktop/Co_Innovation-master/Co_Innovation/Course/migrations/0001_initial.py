# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SystemArticle', '0018_auto_20160814_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cover', models.ImageField(default=b'/static/base/img/picture/JS.jpg', upload_to=b'/course/%Y/%m/%d/', null=True, verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe\xe7\x89\x87', blank=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('time', models.DateTimeField(default=True, null=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
                ('place', models.CharField(default=b'\xe5\x9c\xb0\xe7\x82\xb9', max_length=100, null=True, verbose_name=b'\xe5\x9c\xb0\xe7\x82\xb9')),
                ('course_intro', models.TextField(default=b'\xe6\xa6\x82\xe8\xbf\xb0', verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe6\xa6\x82\xe8\xbf\xb0')),
                ('column', models.ForeignKey(verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae', to='SystemArticle.Column')),
            ],
            options={
                'ordering': ['-time', 'title'],
                'verbose_name': '\u8bfe\u7a0b',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
        ),
    ]
