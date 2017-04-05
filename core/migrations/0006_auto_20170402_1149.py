# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170330_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.CharField(blank=True, help_text='\u041d\u0443\u0436\u043d\u043e \u0434\u043b\u044f \u0421\u0415\u041e', max_length=255, verbose_name='\u041c\u0435\u0442\u0430 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u041c\u0435\u0442\u0430 \u043a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_title',
            field=models.CharField(blank=True, max_length=80, verbose_name='\u041c\u0435\u0442\u0430 title'),
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='\u0421\u0441\u044b\u043b\u043a\u0430 \u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u0440\u0438 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0438.', unique=True),
        ),
    ]