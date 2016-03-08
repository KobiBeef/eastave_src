# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0007_patientnationality'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patientnationality',
            options={'verbose_name_plural': 'Patient Nationality', 'verbose_name': 'Patient Nationality'},
        ),
    ]
