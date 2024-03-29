# Generated by Django 3.1.7 on 2021-02-28 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0005_fleet'),
    ]

    operations = [
        migrations.CreateModel(
            name='subfleet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('fleetid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.fleet')),
            ],
        ),
    ]
