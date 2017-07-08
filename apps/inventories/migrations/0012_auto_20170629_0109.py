# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-06-28 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('niamoto_data', '0022_auto_20170627_0821'),
        ('inventories', '0011_auto_20170627_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxaInventoryTaxon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxa_inventory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventories.TaxaInventory')),
                ('taxon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='taxa', to='niamoto_data.Taxon')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='taxainventorytaxon',
            unique_together=set([('taxa_inventory', 'taxon')]),
        ),
    ]