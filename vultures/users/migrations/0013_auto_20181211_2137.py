# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-11 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='foodpost',
            name='foodPic',
            field=models.ImageField(default='docs/imgs', upload_to=''),
        ),
    ]
