# Generated by Django 2.2.12 on 2020-04-20 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_shape', '0002_auto_20200407_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='legend_locate',
            field=models.CharField(default='bottom', max_length=10),
        ),
        migrations.AddField(
            model_name='graph',
            name='legend_type',
            field=models.IntegerField(default=1),
        ),
    ]
