# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kme', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='raziskava',
            options={'verbose_name_plural': 'raziskave'},
        ),
        migrations.AlterModelOptions(
            name='vlagatelj',
            options={'verbose_name_plural': 'vlagatelji'},
        ),
        migrations.AddField(
            model_name='raziskava',
            name='naslov_raziskave_slo',
            field=models.TextField(blank=True),
        ),
    ]
