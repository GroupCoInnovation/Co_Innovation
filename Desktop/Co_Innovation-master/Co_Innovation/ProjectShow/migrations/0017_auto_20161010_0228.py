# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectShow', '0016_auto_20160901_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='member_project_set', null=True, verbose_name=b'\xe6\x88\x90\xe5\x91\x98', to='User.User'),
        ),
    ]
