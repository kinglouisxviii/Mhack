# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150118_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('EventId', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('Time', models.CharField(max_length=5, null=True)),
                ('Subject', models.CharField(max_length=100, null=True)),
                ('linkedinId', models.CharField(max_length=20, null=True)),
                ('personName', models.CharField(max_length=20, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
