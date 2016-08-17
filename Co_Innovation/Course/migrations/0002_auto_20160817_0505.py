# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='column',
            field=models.ForeignKey(verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae', to='SystemArticle.Column', null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.DateTimeField(verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
