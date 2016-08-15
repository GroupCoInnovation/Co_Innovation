# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20160806_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=b'e10adc3949ba59abbe56e057f20f883e', max_length=100, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81'),
        ),
    ]
