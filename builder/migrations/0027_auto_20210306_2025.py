# Generated by Django 3.1.7 on 2021-03-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0026_a_fleet_b_subfleet_c_wholesaler_d_retailer_e_consumer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='a_fleet',
            old_name='blockchain_addr',
            new_name='blockchain_addr_slug',
        ),
        migrations.AddField(
            model_name='a_fleet',
            name='blockchain_address',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]