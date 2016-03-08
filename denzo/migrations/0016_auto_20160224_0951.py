# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0015_patientinfo_patient_result'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patientinfo',
            options={'verbose_name': 'Patient Info', 'verbose_name_plural': 'Patient Info'},
        ),
        migrations.AlterModelOptions(
            name='physicianinfo',
            options={'verbose_name': 'Physician Info', 'verbose_name_plural': 'Physician Info'},
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='patient_disposition',
            field=models.ForeignKey(blank=True, to='denzo.Disposition', null=True),
        ),
    ]
