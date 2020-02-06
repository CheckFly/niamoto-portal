# Generated by Django 2.2.9 on 2020-01-29 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20200129_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='first_month',
            field=models.IntegerField(blank=True, choices=[('1', 'janvier'), ('2', 'février'), ('3', 'mars'), ('4', 'avril'), ('5', 'mai'), ('6', 'juin'), ('7', 'juillet'), ('8', 'aout'), ('9', 'septembre'), ('10', 'octobre'), ('11', 'novembre'), ('12', 'décembre')], null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='first_year',
            field=models.IntegerField(blank=True, choices=[(2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=2020, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='last_month',
            field=models.IntegerField(blank=True, choices=[('1', 'janvier'), ('2', 'février'), ('3', 'mars'), ('4', 'avril'), ('5', 'mai'), ('6', 'juin'), ('7', 'juillet'), ('8', 'aout'), ('9', 'septembre'), ('10', 'octobre'), ('11', 'novembre'), ('12', 'décembre')], null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='last_year',
            field=models.IntegerField(blank=True, choices=[(2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=2020, null=True),
        ),
    ]