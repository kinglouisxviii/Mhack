# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150117_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.CharField(max_length=16)),
                ('gender', models.CharField(max_length=7)),
                ('linkedIn_id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='WorldBorder',
        ),
    ]
