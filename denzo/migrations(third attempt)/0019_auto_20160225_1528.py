# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0018_auto_20160224_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='attending_physician',
            field=models.ManyToManyField(related_name='attending_phycisian1', blank=True, to='denzo.PhysicianInfo', null=True),
        ),
    ]
