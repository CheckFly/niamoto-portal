# Generated by Django 2.2.12 on 2020-11-16 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_plot', '0007_auto_20201109_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='information',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
    ]
