# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0010_patientbillparty_patientmembership'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patientbillparty',
            options={'verbose_name': 'Party to Pay Bills'},
        ),
        migrations.AlterModelOptions(
            name='patientmembership',
            options={'verbose_name': 'Patient Membership'},
        ),
    ]
