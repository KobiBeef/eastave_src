# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0019_auto_20160225_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='patient_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='patient_birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='patient_informant_relationship',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
