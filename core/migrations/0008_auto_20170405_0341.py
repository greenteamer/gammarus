# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 03:41
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170402_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('slug', models.SlugField(help_text='\u0421\u0441\u044b\u043b\u043a\u0430 \u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u0440\u0438 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0438.', max_length=240, unique=True)),
                ('meta_title', models.CharField(blank=True, max_length=80, verbose_name='\u041c\u0435\u0442\u0430 title')),
                ('meta_description', models.CharField(blank=True, help_text='\u041d\u0443\u0436\u043d\u043e \u0434\u043b\u044f \u0421\u0415\u041e', max_length=255, verbose_name='\u041c\u0435\u0442\u0430 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('meta_keywords', models.CharField(blank=True, max_length=255, verbose_name='\u041c\u0435\u0442\u0430 \u043a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f')),
                ('description', ckeditor.fields.RichTextField()),
                ('preview_description', models.TextField(verbose_name='preview \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('image', models.ImageField(upload_to=b'page')),
            ],
            options={
                'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to=b'news')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.News')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e \u043d\u043e\u0432\u043e\u0441\u0442\u0438',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e \u043d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='', upload_to=b'article'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='certificate',
            field=models.ImageField(default='', upload_to=b'certificate'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(help_text='\u0421\u0441\u044b\u043b\u043a\u0430 \u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u0440\u0438 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0438.', max_length=240, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=240, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='\u0421\u0441\u044b\u043b\u043a\u0430 \u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u0440\u0438 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0438.', max_length=240, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(help_text='\u0421\u0441\u044b\u043b\u043a\u0430 \u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u0440\u0438 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0438.', max_length=240, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(help_text='\u0421\u0441\u044b\u043b\u043a\u0430 \u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u0440\u0438 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0438.', max_length=240, unique=True),
        ),
    ]