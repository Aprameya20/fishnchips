# Generated by Django 3.1.7 on 2021-03-06 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0027_auto_20210306_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='a_fleet',
            name='blockchain_address',
        ),
    ]
