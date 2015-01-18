# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_invite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invite',
            old_name='Subject',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='invite',
            old_name='Time',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='invite',
            name='EventId',
        ),
    ]
