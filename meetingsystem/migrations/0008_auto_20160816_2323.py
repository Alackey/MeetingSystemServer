# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 23:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetingsystem', '0007_auto_20160816_2138'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InviteBox',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]