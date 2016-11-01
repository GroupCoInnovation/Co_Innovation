# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_auto_20160814_0719'),
        ('SystemArticle', '0016_article_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='collect',
        ),
        migrations.AddField(
            model_name='article',
            name='collection',
            field=models.ManyToManyField(default=True, related_name='article_collection', to='User.User', blank=True),
        ),
    ]
