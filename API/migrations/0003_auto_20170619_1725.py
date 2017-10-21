# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_remove_merchant_fucken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='clientGPS',
            new_name='GPS',
        ),
        migrations.RenameField(
            model_name='upload',
            old_name='clientID',
            new_name='fullName',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='callbackStatus',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='idInfoSubmitted',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='merchantInfo',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='selfieImgCreated',
        ),
        migrations.AddField(
            model_name='upload',
            name='idNumber',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='upload',
            name='issPlace',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='upload',
            name='issused',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
