# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0027_auto_20160818_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item004',
            name='field4',
            field=models.CharField(default='.', max_length=200, verbose_name='計劃交貨日期'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='field5',
            field=models.CharField(default='.', max_length=200, verbose_name='客戶需求數'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='field6',
            field=models.CharField(default='.', max_length=200, verbose_name='實際出貨數'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='field7',
            field=models.CharField(default='.', max_length=200, verbose_name='延交數量'),
        ),
    ]