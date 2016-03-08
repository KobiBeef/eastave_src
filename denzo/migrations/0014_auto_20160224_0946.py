# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0013_patientinfo_discharge_doctor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientinfo',
            old_name='discharge_doctor',
            new_name='discharge_physician',
        ),
    ]
