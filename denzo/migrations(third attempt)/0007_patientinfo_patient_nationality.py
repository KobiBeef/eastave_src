# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0006_patientinfo_patient_religion'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='patient_nationality',
            field=models.ForeignKey(to='denzo.Nationality', null=True, blank=True),
        ),
    ]
