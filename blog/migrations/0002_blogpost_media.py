# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]