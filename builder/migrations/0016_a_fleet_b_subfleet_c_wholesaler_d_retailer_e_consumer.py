# Generated by Django 3.1.7 on 2021-03-05 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('builder', '0015_auto_20210306_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='a_fleet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fishName', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField()),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('company', models.CharField(max_length=50)),
                ('blockchain_addr', models.CharField(default='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='b_subfleet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('fleetid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.a_fleet')),
            ],
        ),
        migrations.CreateModel(
            name='c_wholesaler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('subfleetid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.b_subfleet')),
            ],
        ),
        migrations.CreateModel(
            name='d_retailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('wholesalerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.c_wholesaler')),
            ],
        ),
        migrations.CreateModel(
            name='e_consumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('retailerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.d_retailer')),
            ],
        ),
    ]
