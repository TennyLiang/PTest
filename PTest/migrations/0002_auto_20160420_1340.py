# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PTest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='begin_date',
            field=models.DateTimeField(),
        ),
    ]
