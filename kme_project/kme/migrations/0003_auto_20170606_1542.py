# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kme', '0002_auto_20170606_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raziskava',
            name='naslov_raziskave_slo',
            field=models.TextField(default=''),
        ),
    ]
