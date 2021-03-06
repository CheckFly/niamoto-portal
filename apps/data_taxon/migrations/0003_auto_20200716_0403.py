# Generated by Django 2.2.12 on 2020-07-16 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_taxon', '0002_auto_20200407_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='legend_locate',
            field=models.CharField(choices=[('right', 'right'), ('bottom', 'bottom'), ('left', 'left'), ('top', 'top'), ('nolegend', 'nolegend')], default='bottom', max_length=10),
        ),
        migrations.AddField(
            model_name='graph',
            name='legend_type',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='graph',
            name='height',
            field=models.CharField(choices=[('25', 'Small'), ('50', 'Medium'), ('75', 'Large'), ('100', 'XLarge')], default='25', max_length=3),
        ),
    ]
