# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_user_head_image'),
        ('ProjectShow', '0014_project_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='collection',
            field=models.ManyToManyField(default=True, related_name='project_collection', verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f', to='User.User', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='reading_quantity',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\x98\x85\xe8\xaf\xbb\xe9\x87\x8f', blank=True),
        ),
    ]
