# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0008_patientinfo_patient_membership'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='party_to_bill',
            field=models.ForeignKey(null=True, to='denzo.PartyToBill', blank=True),
        ),
    ]
