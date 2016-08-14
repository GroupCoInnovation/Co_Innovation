# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_auto_20160806_0700'),
        ('ProjectShow', '0002_auto_20160806_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='member_project_set', verbose_name=b'\xe6\x88\x90\xe5\x91\x98', to='User.User'),
        ),
    ]
