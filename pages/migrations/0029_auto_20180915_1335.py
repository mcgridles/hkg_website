# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-15 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_auto_20180915_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exppost',
            old_name='link',
            new_name='project_link',
        ),
        migrations.AddField(
            model_name='exppost',
            name='repo_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
