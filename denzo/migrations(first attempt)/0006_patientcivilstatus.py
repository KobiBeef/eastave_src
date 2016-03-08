# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0005_auto_20160223_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientCivilStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('patient_civil_status', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Patient Civil Status',
                'verbose_name_plural': 'Patient Civil Status',
            },
        ),
    ]
