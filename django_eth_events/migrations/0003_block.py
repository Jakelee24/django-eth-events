# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-23 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_eth_events', '0002_daemon_last_error_block_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('block_number', models.IntegerField()),
                ('block_hash', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('decoded_logs', models.TextField(default='[]')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
