# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-11 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20181211_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodpost',
            name='foodType',
            field=models.TextField(max_length=40, verbose_name='Food'),
        ),
    ]
