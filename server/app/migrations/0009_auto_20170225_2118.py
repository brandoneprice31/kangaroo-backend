# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_drive_end_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drive',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]