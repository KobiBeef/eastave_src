# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0007_patientinfo_patient_nationality'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='patient_membership',
            field=models.ForeignKey(to='denzo.Membership', null=True, blank=True),
        ),
    ]
