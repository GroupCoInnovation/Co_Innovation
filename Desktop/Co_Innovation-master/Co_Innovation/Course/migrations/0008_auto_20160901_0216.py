# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0007_auto_20160901_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cover',
            field=models.ImageField(default=b'/static/base/img/picture/JS.jpg', upload_to=b'course/', verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe\xe7\x89\x87'),
        ),
    ]
