# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20160803_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='root',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x99\x90'),
        ),
    ]
