# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('account', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=16)),
                ('nickname', models.CharField(unique=True, max_length=20)),
                ('telno', models.CharField(unique=True, max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('create_date', models.DateField()),
                ('recent_time', models.TimeField()),
            ],
        ),
    ]
