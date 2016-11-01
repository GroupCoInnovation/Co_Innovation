# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_auto_20160806_0826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='root_create',
        ),
        migrations.RemoveField(
            model_name='user',
            name='root_edit',
        ),
        migrations.RemoveField(
            model_name='user',
            name='root_stick',
        ),
        migrations.RemoveField(
            model_name='user',
            name='root_write',
        ),
    ]
