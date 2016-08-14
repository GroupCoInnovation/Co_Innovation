# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='major',
            field=models.CharField(max_length=100, verbose_name=b'\xe4\xb8\x93\xe4\xb8\x9a', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='root',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x9d\x83\xe9\x99\x90'),
        ),
    ]
