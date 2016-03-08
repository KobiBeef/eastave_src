# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0014_patientresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDisposition',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('patient_disposition', models.CharField(null=True, max_length=50, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Patient Disposition',
                'verbose_name': 'Patient Disposition',
            },
        ),
    ]
