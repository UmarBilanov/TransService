# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20180228_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(blank=True, choices=[('new', '\u041d\u043e\u0432\u044b\u0439'), ('cancel', '\u041e\u0442\u043c\u0435\u043d\u0435\u043d'), ('completed', '\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d')], default=None, max_length=64),
        ),
    ]
