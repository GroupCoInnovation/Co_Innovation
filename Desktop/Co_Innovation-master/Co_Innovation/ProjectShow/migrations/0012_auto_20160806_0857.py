# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectShow', '0011_auto_20160806_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe6\x9c\xaa\xe5\xae\x8c\xe6\x88\x90'), (1, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90\xe6\x9c\xaa\xe5\x8f\x91\xe8\xa1\xa8'), (2, b'\xe5\xae\x8c\xe6\x88\x90\xe5\xb9\xb6\xe5\x8f\x91\xe8\xa1\xa8')]),
        ),
    ]
