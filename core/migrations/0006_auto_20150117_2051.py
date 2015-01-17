# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150117_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='linkedIn_id',
            new_name='linkedinId',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AddField(
            model_name='profile',
            name='firstName',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='industry',
            field=models.CharField(max_length=40, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='isActive',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='lastName',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
    ]
