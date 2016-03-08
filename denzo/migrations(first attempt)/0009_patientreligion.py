# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0008_auto_20160223_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientReligion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('patient_religion', models.CharField(blank=True, null=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Religion',
            },
        ),
    ]
