# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0029_auto_20160225_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_gender',
            field=models.CharField(max_length=10, blank=True, null=True),
        ),
    ]
