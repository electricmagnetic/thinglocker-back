# Generated by Django 3.0.5 on 2020-05-03 00:42

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('frequency', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('modulation', models.CharField(blank=True, max_length=4, null=True)),
                ('data_rate', models.CharField(blank=True, max_length=7, null=True)),
                ('bit_rate', models.IntegerField(blank=True, null=True)),
                ('coding_rate', models.CharField(blank=True, max_length=3, null=True)),
                ('gateways', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)),
                ('altitude', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Datum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.CharField(max_length=36)),
                ('dev_id', models.CharField(max_length=36)),
                ('hardware_serial', models.CharField(blank=True, max_length=16, null=True)),
                ('port', models.IntegerField(blank=True, null=True)),
                ('counter', models.IntegerField(blank=True, null=True)),
                ('is_retry', models.BooleanField(null=True)),
                ('confirmed', models.BooleanField(null=True)),
                ('payload_raw', models.CharField(blank=True, max_length=128, null=True)),
                ('payload_fields', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('downlink_url', models.URLField(blank=True, max_length=255, null=True)),
                ('metadata', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data.Metadata')),
            ],
        ),
    ]
