# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-18 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_auto_20170525_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='exppost',
            name='details',
            field=models.TextField(null=True),
        ),
    ]
