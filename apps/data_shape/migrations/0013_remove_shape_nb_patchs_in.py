# Generated by Django 2.2.12 on 2020-10-22 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_shape', '0012_auto_20201022_0408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shape',
            name='nb_patchs_in',
        ),
    ]
