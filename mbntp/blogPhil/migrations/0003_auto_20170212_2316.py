# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-12 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPhil', '0002_auto_20170211_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='general', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='mot_en',
            field=models.CharField(max_length=100),
        ),
    ]
