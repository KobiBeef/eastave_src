# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='patient_service',
            field=models.ForeignKey(blank=True, to='denzo.Service', null=True),
        ),
    ]
