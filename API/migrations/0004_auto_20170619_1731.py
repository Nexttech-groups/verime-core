# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_auto_20170619_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='callLog',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='upload',
            name='phoneBook',
            field=models.TextField(null=True),
        ),
    ]
