# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-09 18:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wlink', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
    ]
