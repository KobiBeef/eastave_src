# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0024_auto_20160225_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='test',
            name='patient',
        ),
    ]
