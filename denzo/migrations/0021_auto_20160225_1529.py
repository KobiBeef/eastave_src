# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0020_auto_20160225_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='resident_in_charge',
            field=models.ManyToManyField(null=True, blank=True, related_name='resident_physician', to='denzo.PhysicianInfo'),
        ),
    ]
