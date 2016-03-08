# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0012_auto_20160223_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientClassification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('patient_class', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
    ]
