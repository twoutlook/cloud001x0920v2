# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0037_item003v2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item003v2',
            name='headerd',
            field=models.DateTimeField(),
        ),
    ]
