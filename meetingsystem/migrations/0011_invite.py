# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetingsystem', '0010_delete_invitebox'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(db_index=True, max_length=20)),
                ('meetingOwner', models.CharField(max_length=20)),
                ('meetingId', models.IntegerField()),
                ('title', models.CharField(max_length=120)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('date', models.DateField()),
            ],
        ),
    ]
