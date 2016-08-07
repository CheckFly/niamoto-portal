# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-07 22:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('niamoto_data', '0004_auto_20160802_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlotOccurrences',
            fields=[
                ('occurrence_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='niamoto_data.Occurrence')),
                ('plot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='niamoto_data.Plot')),
            ],
        ),
    ]
