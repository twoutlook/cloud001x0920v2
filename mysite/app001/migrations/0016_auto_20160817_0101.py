# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0015_auto_20160817_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item001',
            name='field4',
        ),
        migrations.RemoveField(
            model_name='item001',
            name='field5',
        ),
        migrations.RemoveField(
            model_name='item001',
            name='field6',
        ),
        migrations.RemoveField(
            model_name='item001',
            name='field7',
        ),
        migrations.AddField(
            model_name='item001',
            name='field4a',
            field=models.CharField(default='.', max_length=200, verbose_name='進度一'),
        ),
        migrations.AddField(
            model_name='item001',
            name='field4b',
            field=models.CharField(default='.', max_length=200, verbose_name='進度二'),
        ),
        migrations.AddField(
            model_name='item001',
            name='field4c',
            field=models.CharField(default='.', max_length=200, verbose_name='進度三'),
        ),
        migrations.AlterField(
            model_name='item001',
            name='field3',
            field=models.CharField(default='.', max_length=200, verbose_name='零件'),
        ),
    ]
