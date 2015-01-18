# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150118_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invite',
            name='personName',
        ),
        migrations.AddField(
            model_name='invite',
            name='place',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
    ]
