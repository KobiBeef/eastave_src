# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0021_auto_20160225_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='physician',
            field=models.ManyToManyField(null=True, to='denzo.PhysicianInfo', related_name='attending_physician2', blank=True),
        ),
    ]
