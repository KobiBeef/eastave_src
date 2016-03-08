# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0004_auto_20160224_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='patient_civil_status',
            field=models.ForeignKey(to='denzo.CivilStatus', null=True, blank=True),
        ),
    ]
