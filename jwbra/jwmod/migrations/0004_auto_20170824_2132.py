# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jwmod', '0003_jwbra'),
    ]

    operations = [
        migrations.CreateModel(
            name='JwSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(default='75B', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='jwbra',
            name='size_name',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='jwmod.JwSize'),
            preserve_default=False,
        ),
    ]