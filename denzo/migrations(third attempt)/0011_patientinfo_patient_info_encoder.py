# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0010_auto_20160224_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='patient_info_encoder',
            field=models.ForeignKey(to='denzo.Encoder', null=True, blank=True),
        ),
    ]
