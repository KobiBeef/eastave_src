# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0030_auto_20160226_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInfo2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_admission', models.DateField(null=True, blank=True)),
                ('hospital_number', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('age', models.IntegerField(null=True, blank=True)),
                ('gender', models.CharField(max_length=50, null=True, blank=True)),
                ('category', models.CharField(max_length=50, null=True, blank=True)),
                ('icd_10', models.IntegerField(null=True, blank=True)),
                ('admitting_dxg', models.TextField(null=True, blank=True)),
                ('final_dxg', models.TextField(null=True, blank=True)),
                ('disposition', models.CharField(max_length=50, null=True, blank=True)),
                ('date_of_discharge', models.DateField(null=True, blank=True)),
                ('hospital_stay', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Patient Info 2',
                'verbose_name': 'Patient Info 2',
            },
        ),
    ]
