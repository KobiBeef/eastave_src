# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0027_auto_20160225_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_gender',
            field=models.ForeignKey(to='denzo.Gender', blank=True, null=True),
        ),
    ]
