# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SystemArticle', '0009_article_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cover',
            field=models.ImageField(default=b'/static/img/picture/pageR.png', upload_to=b'./user/%Y/%m.%d/', verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
    ]
