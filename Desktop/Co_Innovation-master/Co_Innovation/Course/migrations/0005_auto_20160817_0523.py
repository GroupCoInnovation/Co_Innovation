# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0004_remove_course_course_intro'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '\u8bfe\u7a0b', 'verbose_name_plural': '\u8bfe\u7a0b'},
        ),
        migrations.AddField(
            model_name='course',
            name='course_intro',
            field=models.TextField(default=b'\xe6\xa6\x82\xe8\xbf\xb0', verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe6\xa6\x82\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='course',
            name='cover',
            field=models.ImageField(default=b'/static/base/img/picture/JS.jpg', upload_to=b'/course/', verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='course',
            name='place',
            field=models.CharField(default=b'\xe5\x9c\xb0\xe7\x82\xb9', max_length=100, verbose_name=b'\xe5\x9c\xb0\xe7\x82\xb9'),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.DateTimeField(verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
