# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
