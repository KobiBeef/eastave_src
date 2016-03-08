# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0006_patientcivilstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientNationality',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('patient_nationality', models.CharField(null=True, max_length=50, blank=True)),
            ],
        ),
    ]
