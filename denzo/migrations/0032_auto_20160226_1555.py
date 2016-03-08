# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0031_patientinfo2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientinfo2',
            old_name='hospital_stay',
            new_name='hospital_stay_in_days',
        ),
        migrations.AlterField(
            model_name='patientinfo2',
            name='icd_10',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
