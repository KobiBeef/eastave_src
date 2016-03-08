# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0003_patientinfo_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientinfo',
            old_name='gender',
            new_name='patient_gender',
        ),
    ]
