# Generated by Django 2.2.12 on 2020-07-21 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_shape', '0008_auto_20200520_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequency',
            name='class_name',
            field=models.CharField(max_length=100),
        ),
    ]
