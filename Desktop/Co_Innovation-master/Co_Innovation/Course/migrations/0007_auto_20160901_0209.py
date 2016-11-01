# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0006_auto_20160817_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_intro',
        ),
        migrations.AddField(
            model_name='course',
            name='content',
            field=models.TextField(default=b'\xe6\xa6\x82\xe8\xbf\xb0', verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe6\xa6\x82\xe8\xbf\xb0'),
        ),
        migrations.AddField(
            model_name='course',
            name='speaker',
            field=models.CharField(default=b'\xe4\xb8\xbb\xe8\xae\xb2\xe4\xba\xba', max_length=100, verbose_name=b'\xe4\xb8\xbb\xe8\xae\xb2\xe4\xba\xba'),
        ),
        migrations.AddField(
            model_name='course',
            name='summary',
            field=models.TextField(default=b'\xe6\x91\x98\xe8\xa6\x81', verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe6\x91\x98\xe8\xa6\x81'),
        ),
    ]
