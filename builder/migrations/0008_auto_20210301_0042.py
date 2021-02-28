# Generated by Django 3.1.7 on 2021-02-28 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0007_consumer_retailer_wholesaler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retailer',
            name='wholesalerid',
        ),
        migrations.RemoveField(
            model_name='subfleet',
            name='fleetid',
        ),
        migrations.RemoveField(
            model_name='wholesaler',
            name='subfleetid',
        ),
        migrations.DeleteModel(
            name='consumer',
        ),
        migrations.DeleteModel(
            name='fleet',
        ),
        migrations.DeleteModel(
            name='retailer',
        ),
        migrations.DeleteModel(
            name='subfleet',
        ),
        migrations.DeleteModel(
            name='wholesaler',
        ),
    ]
