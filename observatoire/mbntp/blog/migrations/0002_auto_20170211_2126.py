# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-11 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mot_en', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='entree',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
