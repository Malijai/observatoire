# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-08 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bottin', '0005_auto_20170608_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ressource',
            name='document',
        ),
        migrations.AddField(
            model_name='document',
            name='ressource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bottin.Ressource'),
        ),
    ]
