# Generated by Django 2.2.12 on 2020-11-18 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0021_delete_siteinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateUpdateData', models.DateField()),
            ],
        ),
    ]