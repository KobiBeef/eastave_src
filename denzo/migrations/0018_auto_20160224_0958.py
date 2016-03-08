# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0017_auto_20160224_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='admission_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
