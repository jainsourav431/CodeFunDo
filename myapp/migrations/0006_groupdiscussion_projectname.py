# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-07 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20180106_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupdiscussion',
            name='projectName',
            field=models.CharField(default='', max_length=100),
        ),
    ]