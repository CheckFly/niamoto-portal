# Generated by Django 2.2.9 on 2020-01-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20200129_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='title',
            field=models.CharField(blank=True, default=' ', max_length=150, null=True),
        ),
    ]
