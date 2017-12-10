# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 12:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jwmod', '0012_auto_20170831_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='jwstocklist',
            name='price',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='jwsalesbill',
            name='sale_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 31, 12, 51, 2, 681723, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jwstocklist',
            name='stock_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 31, 12, 51, 2, 679723, tzinfo=utc)),
        ),
    ]
