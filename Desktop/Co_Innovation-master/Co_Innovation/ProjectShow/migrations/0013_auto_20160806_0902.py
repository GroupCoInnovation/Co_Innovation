# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectShow', '0012_auto_20160806_0857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['status', 'project_name'], 'verbose_name': '\u9879\u76ee', 'verbose_name_plural': '\u9879\u76ee'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['is_finished', 'project'], 'verbose_name': '\u4efb\u52a1', 'verbose_name_plural': '\u4efb\u52a1'},
        ),
    ]
