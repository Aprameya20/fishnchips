# Generated by Django 3.1.7 on 2021-03-06 16:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0028_remove_a_fleet_blockchain_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='a_fleet',
            old_name='blockchain_addr_slug',
            new_name='blockchain_address',
        ),
        migrations.AddField(
            model_name='b_subfleet',
            name='blockchain_address',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='c_wholesaler',
            name='blockchain_address',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='d_retailer',
            name='blockchain_address',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='e_consumer',
            name='blockchain_address',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
