# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-15 20:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='verifycode',
            options={'verbose_name': '手机验证码信息', 'verbose_name_plural': '手机验证码信息'},
        ),
    ]
