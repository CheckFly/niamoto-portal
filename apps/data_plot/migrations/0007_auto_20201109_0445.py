# Generated by Django 2.2.12 on 2020-11-09 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_plot', '0006_auto_20200916_0408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plot',
            old_name='biomasse',
            new_name='biomass',
        ),
        migrations.RenameField(
            model_name='plot',
            old_name='wood_density',
            new_name='wood_density_mean',
        ),
    ]
