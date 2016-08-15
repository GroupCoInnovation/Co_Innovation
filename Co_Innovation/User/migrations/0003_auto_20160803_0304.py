# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20160801_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='root_create',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe7\x94\xa8\xe6\x88\xb7'),
        ),
        migrations.AddField(
            model_name='user',
            name='root_edit',
            field=models.BooleanField(default=False, verbose_name=b'\xe7\xbc\x96\xe8\xbe\x91\xe4\xb8\x8e\xe5\x88\xa0\xe9\x99\xa4'),
        ),
        migrations.AddField(
            model_name='user',
            name='root_stick',
            field=models.BooleanField(default=False, verbose_name=b'\xe7\xbd\xae\xe9\xa1\xb6'),
        ),
        migrations.AddField(
            model_name='user',
            name='root_write',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x86\x99\xe6\x96\x87\xe7\xab\xa0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=b'123456', max_length=100, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81'),
        ),
    ]
