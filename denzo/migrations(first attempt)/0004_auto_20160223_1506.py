# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0003_patientservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientGender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('gender', models.CharField(max_length=10, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Gender',
            },
        ),
        migrations.AlterModelOptions(
            name='patientservice',
            options={'verbose_name': 'Patient Service', 'verbose_name_plural': 'Patient Service'},
        ),
    ]
