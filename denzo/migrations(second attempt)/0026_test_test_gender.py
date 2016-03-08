# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0025_auto_20160225_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test_gender',
            field=models.ForeignKey(to='denzo.Gender', null=True, blank=True),
        ),
    ]
