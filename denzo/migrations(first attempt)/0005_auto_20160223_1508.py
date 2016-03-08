# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0004_auto_20160223_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientgender',
            old_name='gender',
            new_name='patient_gender',
        ),
    ]
