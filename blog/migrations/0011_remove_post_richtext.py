# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 20:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_richtextuploads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='richtext',
        ),
    ]
