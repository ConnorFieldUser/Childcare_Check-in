# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0007_remove_child_on_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
