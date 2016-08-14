# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectShow', '0006_auto_20160806_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xb6\xe9\x97\xb4', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
