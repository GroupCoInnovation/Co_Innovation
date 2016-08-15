# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_auto_20160814_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='head_image',
            field=models.ImageField(default=b'/static/base/img/index/Avatar.png', upload_to=b'./user/%Y/%m/%d/', null=True, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f', blank=True),
        ),
    ]
