# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SystemArticle', '0014_auto_20160813_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='cover',
        ),
    ]
