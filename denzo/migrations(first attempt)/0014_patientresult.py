# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0013_patientclassification'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientResult',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('patient_result', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Patient Result',
                'verbose_name': 'Patient Result',
            },
        ),
    ]
