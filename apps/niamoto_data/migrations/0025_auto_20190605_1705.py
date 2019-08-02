# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-05 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niamoto_data', '0024_auto_20180202_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxon',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]