# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150118_0900'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Invite',
        ),
    ]
