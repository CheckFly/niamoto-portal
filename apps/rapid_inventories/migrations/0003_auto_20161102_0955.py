# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-01 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rapid_inventories', '0002_inventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rapidinventory',
            old_name='id',
            new_name='inventory_ptr'
        ),
        migrations.RemoveField(
            model_name='rapidinventory',
            name='inventory_date',
        ),
        migrations.RemoveField(
            model_name='rapidinventory',
            name='location',
        ),
        migrations.RemoveField(
            model_name='rapidinventory',
            name='observer',
        ),
        # migrations.AddField(
        #     model_name='rapidinventory',
        #     name='inventory_ptr',
        #     field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rapid_inventories.Inventory'),
        #     preserve_default=False,
        # ),
    ]
