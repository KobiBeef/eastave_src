# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0005_patientinfo_patient_civil_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='patient_religion',
            field=models.ForeignKey(null=True, blank=True, to='denzo.Religion'),
        ),
    ]
