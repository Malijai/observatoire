# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-12 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170212_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
