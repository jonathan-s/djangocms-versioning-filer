# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-02 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    def __init__(self, name, app_label):
        super(Migration, self).__init__(name, 'filer')

    dependencies = [
        ('djangocms_versioning', '0010_version_proxies'),
        ('djangocms_versioning_filer', '0001_initial'),
        ('filer', '0010_auto_20180414_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='grouper',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='djangocms_versioning_filer.FileGrouper'),
        ),
    ]

    replaces = (('filer', __module__.rsplit('.', 1)[-1]),)
