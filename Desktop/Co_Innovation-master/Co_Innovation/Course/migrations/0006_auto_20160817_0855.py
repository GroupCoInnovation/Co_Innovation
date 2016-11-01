# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0005_auto_20160817_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.DateTimeField(null=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
