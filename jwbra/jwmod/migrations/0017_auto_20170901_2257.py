# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 14:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jwmod', '0016_auto_20170901_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='jwsalesbill',
            name='total',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='jwsalesbill',
            name='sale_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 1, 14, 57, 51, 574211, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jwstocklist',
            name='stock_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 1, 14, 57, 51, 572211, tzinfo=utc)),
        ),
    ]