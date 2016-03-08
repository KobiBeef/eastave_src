# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientName',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('pt_no', models.IntegerField(unique=True)),
                ('pt_last_name', models.CharField(max_length=100)),
                ('pt_first_name', models.CharField(max_length=100)),
                ('pt_middle_name', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=100)),
                ('pt_birthdate', models.DateField()),
                ('pt_age', models.IntegerField()),
                ('pt_sex', models.CharField(max_length=5)),
                ('pt_status', models.CharField(max_length=15)),
                ('pt_nationality', models.CharField(max_length=20)),
                ('pt_religion', models.CharField(max_length=20)),
                ('pt_home_add', models.TextField()),
                ('pt_office_add', models.TextField(null=True)),
                ('pt_occupation', models.CharField(null=True, max_length=20)),
                ('pt_emloyer', models.CharField(null=True, max_length=100)),
                ('pt_membership', models.CharField(null=True, max_length=50)),
                ('pt_fthr_last_name', models.CharField(max_length=100)),
                ('pt_fthr_first_name', models.CharField(max_length=100)),
                ('pt_mthr_last_name', models.CharField(max_length=100)),
                ('pt_mthr_first_name', models.CharField(max_length=100)),
                ('pt_spouse_last_name', models.CharField(max_length=100)),
                ('pt_spouse_first_name', models.CharField(max_length=100)),
                ('pt_spouse_middle_name', models.CharField(max_length=100)),
                ('mode_payment', models.CharField(max_length=100)),
                ('admitting_dxg', models.TextField()),
                ('admission_date', models.DateTimeField(auto_now_add=True)),
                ('ward', models.CharField(max_length=50)),
                ('room_no', models.IntegerField(null=True)),
                ('bed_no', models.IntegerField(null=True)),
                ('encoder_last_name', models.CharField(max_length=100)),
                ('encoder_first_name', models.CharField(max_length=100)),
                ('encoder_middiel_initial', models.CharField(max_length=5)),
                ('pt_class', models.CharField(max_length=20)),
                ('pt_informant_first_name', models.CharField(null=True, max_length=100)),
                ('pt_informant_last_name', models.CharField(null=True, max_length=100)),
                ('pt_informant_relationship', models.CharField(null=True, max_length=100)),
                ('final_dxg', models.TextField()),
                ('implication', models.TextField()),
                ('code', models.IntegerField(null=True)),
                ('pt_result', models.CharField(max_length=100)),
                ('pt_disposition', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=300, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Patients',
                'verbose_name': 'Patient',
            },
        ),
        migrations.CreateModel(
            name='PhysicianName',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('dr_last_name', models.CharField(max_length=100)),
                ('dr_first_name', models.CharField(max_length=100)),
                ('dr_middle_initial', models.CharField(max_length=3)),
                ('slug', models.SlugField(max_length=300, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Doctors',
                'verbose_name': 'Doctor',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('doctor', models.ManyToManyField(to='denzo.PhysicianName')),
                ('patient', models.ForeignKey(to='denzo.PatientName')),
            ],
            options={
                'verbose_name_plural': 'Tests',
                'verbose_name': 'Test',
            },
        ),
        migrations.AddField(
            model_name='patientname',
            name='attending_physician',
            field=models.ManyToManyField(to='denzo.PhysicianName', related_name='attending_physician2'),
        ),
        migrations.AddField(
            model_name='patientname',
            name='physician',
            field=models.ManyToManyField(to='denzo.PhysicianName', related_name='attending_phycisian1'),
        ),
        migrations.AddField(
            model_name='patientname',
            name='resident_in_charge',
            field=models.ManyToManyField(to='denzo.PhysicianName', related_name='resident_physician'),
        ),
    ]
