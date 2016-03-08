# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0011_auto_20160223_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encoder',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('encoder_last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('encoder_first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('encoder_middle_initial', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Encoder',
                'verbose_name_plural': 'Encoders',
            },
        ),
        migrations.AlterModelOptions(
            name='patientbillparty',
            options={'verbose_name': 'Party to Pay Bill', 'verbose_name_plural': 'Party to Pay Bill'},
        ),
        migrations.AlterModelOptions(
            name='patientmembership',
            options={'verbose_name': 'Patient Membership', 'verbose_name_plural': 'Patient Membership'},
        ),
        migrations.AlterModelOptions(
            name='patientreligion',
            options={'verbose_name': 'Religion', 'verbose_name_plural': 'Religion'},
        ),
    ]
