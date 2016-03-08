# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0023_auto_20160225_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='attending_physician',
            field=models.ManyToManyField(related_name='attending_phycisian1', to='denzo.PhysicianInfo', blank=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='physician',
            field=models.ManyToManyField(related_name='attending_physician2', to='denzo.PhysicianInfo', blank=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='resident_in_charge',
            field=models.ManyToManyField(related_name='resident_physician', to='denzo.PhysicianInfo', blank=True),
        ),
    ]
