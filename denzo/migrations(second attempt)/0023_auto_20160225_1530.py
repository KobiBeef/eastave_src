# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0022_auto_20160225_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='slug',
            field=models.SlugField(max_length=300, null=True, blank=True, unique=True),
        ),
    ]
