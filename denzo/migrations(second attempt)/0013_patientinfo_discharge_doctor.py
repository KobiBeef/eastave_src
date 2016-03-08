# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0012_patientinfo_patient_mother_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='discharge_doctor',
            field=models.ForeignKey(null=True, to='denzo.PhysicianInfo', related_name='discharge_physician', blank=True),
        ),
    ]
