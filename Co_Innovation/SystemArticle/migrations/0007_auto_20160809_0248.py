# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SystemArticle', '0006_auto_20160807_0545'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['category', '-top', '-top_time', 'pub_date'], 'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='column',
            options={'ordering': ['category', 'column_name'], 'verbose_name': '\u680f\u76ee', 'verbose_name_plural': '\u680f\u76ee'},
        ),
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(default=b'\xe6\x91\x98\xe8\xa6\x81', null=True, verbose_name=b'\xe6\x91\x98\xe8\xa6\x81', blank=True),
        ),
    ]
