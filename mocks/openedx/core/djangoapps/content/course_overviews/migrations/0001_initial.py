# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-03 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import opaque_keys.edx.django.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseOverview',
            fields=[
                ('id', opaque_keys.edx.django.models.CourseKeyField(db_index=True, max_length=255, primary_key=True, serialize=False)),
                ('display_name', models.TextField(null=True)),
                ('org', models.TextField(max_length=255)),
                ('number', models.TextField()),
            ],
        ),
    ]
