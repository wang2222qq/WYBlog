# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('pub_time', models.DateTimeField()),
                ('lable', models.CharField(max_length=60)),
                ('browes_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.IntegerField(serialize=False, primary_key=True)),
                ('nickname', models.CharField(max_length=20)),
                ('contents', models.CharField(max_length=200)),
                ('create_time', models.DateTimeField()),
                ('forgein_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Photoalbum',
            fields=[
                ('album_id', models.IntegerField(serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=60)),
                ('pub_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Photograph',
            fields=[
                ('photo_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('image_address', models.FileField(upload_to=b'')),
                ('pub_time', models.DateTimeField()),
                ('browes_number', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='PersonInfo',
        ),
    ]
