# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0002_item000_item001_item002_item003_item004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=200)),
                ('field2', models.CharField(max_length=200)),
                ('field3', models.CharField(max_length=200)),
                ('field4', models.CharField(max_length=200)),
                ('field5', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
