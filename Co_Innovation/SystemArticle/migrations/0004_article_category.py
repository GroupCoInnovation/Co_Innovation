# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SystemArticle', '0003_auto_20160807_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default=b'SA', max_length=20, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xb1\xbb\xe5\x88\xab', choices=[(b'SA', b'\xe7\xb3\xbb\xe7\xbb\x9f\xe6\x96\x87\xe7\xab\xa0'), (b'CA', b'\xe8\xaf\xbe\xe7\xa8\x8b\xe6\x96\x87\xe7\xab\xa0')]),
        ),
    ]
