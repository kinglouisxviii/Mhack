# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150117_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='linkedIn_id',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
