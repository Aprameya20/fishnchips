# Generated by Django 3.1.7 on 2021-03-06 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0024_auto_20210306_0141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='b_subfleet',
            name='fleetid',
        ),
        migrations.RemoveField(
            model_name='c_wholesaler',
            name='subfleetid',
        ),
        migrations.RemoveField(
            model_name='d_retailer',
            name='wholesalerid',
        ),
        migrations.RemoveField(
            model_name='e_consumer',
            name='retailerid',
        ),
        migrations.DeleteModel(
            name='a_fleet',
        ),
        migrations.DeleteModel(
            name='b_subfleet',
        ),
        migrations.DeleteModel(
            name='c_wholesaler',
        ),
        migrations.DeleteModel(
            name='d_retailer',
        ),
        migrations.DeleteModel(
            name='e_consumer',
        ),
    ]
