# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectShow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='principal',
            field=models.ForeignKey(related_name='principal_project_set', verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba', to='User.User'),
        ),
    ]
