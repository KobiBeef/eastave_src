# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0009_patientreligion'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientBillParty',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('patient_bill_party', models.CharField(max_length=50, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('patient_membership', models.CharField(max_length=50, blank=True, null=True)),
            ],
        ),
    ]
