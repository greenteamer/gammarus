# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20170303_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
