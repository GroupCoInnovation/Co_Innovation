# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'SA', max_length=20, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xb1\xbb\xe5\x88\xab', choices=[(b'SA', b'\xe7\xb3\xbb\xe7\xbb\x9f\xe6\x96\x87\xe7\xab\xa0'), (b'CA', b'\xe8\xaf\xbe\xe7\xa8\x8b\xe6\x96\x87\xe7\xab\xa0')])),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('content', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('reading_quantity', models.IntegerField(default=0, verbose_name=b'\xe9\x98\x85\xe8\xaf\xbb\xe9\x87\x8f', blank=True)),
                ('collect', models.IntegerField(default=0, verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f', blank=True)),
                ('top', models.BooleanField(default=False, verbose_name=b'\xe7\xbd\xae\xe9\xa1\xb6')),
                ('top_time', models.DateTimeField(verbose_name=b'\xe7\xbd\xae\xe9\xa1\xb6\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ['-top', '-top_time', 'pub_date'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'SC', max_length=20, verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae\xe7\xb1\xbb\xe5\x88\xab', choices=[(b'SC', b'\xe7\xb3\xbb\xe7\xbb\x9f\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x8f\xe7\x9b\xae'), (b'CC', b'\xe8\xaf\xbe\xe7\xa8\x8b\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x8f\xe7\x9b\xae')])),
                ('column_name', models.CharField(max_length=250, verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('column_text', models.CharField(max_length=250, verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae\xe7\xae\x80\xe4\xbb\x8b', blank=True)),
            ],
            options={
                'ordering': ['column_name'],
                'verbose_name': '\u680f\u76ee',
                'verbose_name_plural': '\u680f\u76ee',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ForeignKey(default=True, verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae', to='SystemArticle.Column'),
        ),
    ]
