# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0002_patientinfo_patient_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='gender',
            field=models.ForeignKey(to='denzo.Gender', null=True, blank=True),
        ),
    ]
