# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0002_auto_20160223_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientService',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('patient_service', models.CharField(null=True, blank=True, max_length=50)),
            ],
        ),
    ]
