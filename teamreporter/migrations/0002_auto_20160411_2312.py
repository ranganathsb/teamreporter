# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 23:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teamreporter', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('user', 'team')]),
        ),
    ]
