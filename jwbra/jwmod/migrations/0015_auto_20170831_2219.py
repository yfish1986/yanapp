# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 14:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jwmod', '0014_auto_20170831_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jwsalesbill',
            name='sale_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 31, 14, 19, 44, 156094, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jwstocklist',
            name='stock_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 31, 14, 19, 44, 155094, tzinfo=utc)),
        ),
    ]