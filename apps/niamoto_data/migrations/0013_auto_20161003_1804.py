# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-03 07:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('niamoto_data', '0012_auto_20160930_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occurrenceobservations',
            name='id',
        ),
        migrations.AlterField(
            model_name='occurrenceobservations',
            name='occurrence',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='observations', serialize=False, to='niamoto_data.Occurrence'),
        ),
    ]