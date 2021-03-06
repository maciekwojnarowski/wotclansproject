# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wotclans', '0003_auto_20171105_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='clan',
            name='description_html',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='clan',
            name='motto',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='statistics_gm10',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='statistics_gm6',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='statistics_gm8',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='statistics_random',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='statistics_sh_defense',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='statistics_skirmishes',
            field=models.TextField(default=''),
        ),
    ]
