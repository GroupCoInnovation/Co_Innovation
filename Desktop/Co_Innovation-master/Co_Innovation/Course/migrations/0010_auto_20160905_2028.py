# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0009_auto_20160901_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='collection',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f'),
        ),
        migrations.AddField(
            model_name='course',
            name='like',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x96\x9c\xe6\xac\xa2'),
        ),
        migrations.AddField(
            model_name='course',
            name='reading_quantity',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\x98\x85\xe8\xaf\xbb\xe9\x87\x8f'),
        ),
    ]
