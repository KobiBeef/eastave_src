# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0014_auto_20160224_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='patient_result',
            field=models.ForeignKey(blank=True, null=True, to='denzo.Result'),
        ),
    ]
