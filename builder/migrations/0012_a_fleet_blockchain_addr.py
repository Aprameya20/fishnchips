# Generated by Django 3.1.7 on 2021-03-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0011_a_fleet_b_subfleet_c_wholesaler_d_retailer_e_consumer'),
    ]

    operations = [
        migrations.AddField(
            model_name='a_fleet',
            name='blockchain_addr',
            field=models.CharField(default='bKFVKSDFKJS12323', max_length=32),
        ),
    ]
