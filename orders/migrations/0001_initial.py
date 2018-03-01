# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('surname', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('phone', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('date_time', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b',
            },
        ),
    ]
