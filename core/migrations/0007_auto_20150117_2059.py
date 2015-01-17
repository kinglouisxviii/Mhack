# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150117_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='longitude',
            new_name='longtitude',
        ),
    ]
