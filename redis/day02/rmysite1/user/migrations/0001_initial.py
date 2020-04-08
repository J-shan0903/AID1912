# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-07 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='', max_length=11, verbose_name='昵称')),
                ('age', models.IntegerField(default=0, verbose_name='年龄')),
            ],
        ),
    ]
