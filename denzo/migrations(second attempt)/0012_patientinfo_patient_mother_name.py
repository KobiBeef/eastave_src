# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0011_patientinfo_patient_info_encoder'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='patient_mother_name',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
    ]
