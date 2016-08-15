# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectShow', '0004_remove_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe9\xa1\xb9\xe7\x9b\xae', to='ProjectShow.Project', null=True),
        ),
    ]
