# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_auto_20160806_0826'),
        ('SystemArticle', '0007_auto_20160809_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe4\xbd\x9c\xe8\x80\x85', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='pub_user',
            field=models.ForeignKey(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe8\x80\x85', blank=True, to='User.User', null=True),
        ),
    ]
