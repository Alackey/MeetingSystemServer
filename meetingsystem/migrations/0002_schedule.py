# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 06:31
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetingsystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('employeeID', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('blocks', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(), size=None)),
            ],
        ),
    ]
