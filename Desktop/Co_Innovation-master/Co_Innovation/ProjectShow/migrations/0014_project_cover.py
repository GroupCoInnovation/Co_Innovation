# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectShow', '0013_auto_20160806_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cover',
            field=models.ImageField(default=b'/static/base/img/index/new-class.jpg', upload_to=b'./project/', verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe\xe7\x89\x87'),
        ),
    ]
