# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewshare', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='id',
        ),
        migrations.AlterField(
            model_name='paper',
            name='doi',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
