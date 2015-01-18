# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_delete_invite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('eventid', models.IntegerField(default=1, serialize=False, primary_key=True)),
                ('time', models.CharField(max_length=5, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('linkedinId', models.CharField(max_length=20, null=True)),
                ('place', models.CharField(max_length=25, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
