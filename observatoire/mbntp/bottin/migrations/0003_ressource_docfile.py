# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-08 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottin', '0002_ressource_popcible'),
    ]

    operations = [
        migrations.AddField(
            model_name='ressource',
            name='docfile',
            field=models.FileField(default=1, upload_to='DocsRessources/'),
            preserve_default=False,
        ),
    ]