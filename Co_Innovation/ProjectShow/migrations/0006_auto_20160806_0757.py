# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectShow', '0005_task_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='worker',
            field=models.ForeignKey(verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe8\x80\x85', to='User.User', null=True),
        ),
    ]
