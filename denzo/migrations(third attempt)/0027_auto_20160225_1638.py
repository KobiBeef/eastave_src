# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0026_test_test_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_gender',
            field=models.CharField(blank=True, null=True, max_length=10),
        ),
    ]
