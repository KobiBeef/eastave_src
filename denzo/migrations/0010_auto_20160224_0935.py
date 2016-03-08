# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0009_patientinfo_party_to_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='patient_classification',
            field=models.ForeignKey(null=True, to='denzo.Classification', blank=True),
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='rate',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
