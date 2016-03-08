# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CivilStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('civil_status', models.CharField(null=True, max_length=50, blank=True)),
            ],
            options={
                'verbose_name': 'Civil Status',
                'verbose_name_plural': 'Civil Status',
            },
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('payment_class', models.CharField(null=True, max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disposition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('disposition', models.CharField(null=True, max_length=50, blank=True)),
            ],
            options={
                'verbose_name': 'Disposition',
                'verbose_name_plural': 'Disposition',
            },
        ),
        migrations.CreateModel(
            name='Encoder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('encoder_last_name', models.CharField(null=True, max_length=50, blank=True)),
                ('encoder_first_name', models.CharField(null=True, max_length=50, blank=True)),
                ('encoder_middle_initial', models.CharField(null=True, max_length=50, blank=True)),
            ],
            options={
                'verbose_name': 'Encoder',
                'verbose_name_plural': 'Encoders',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('gender', models.CharField(null=True, max_length=10, blank=True)),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Gender',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('membership', models.CharField(null=True, max_length=50, blank=True)),
            ],
            options={
                'verbose_name': 'Membership',
                'verbose_name_plural': 'Membership',
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nationality', models.CharField(null=True, max_length=50, blank=True)),
            ],
            options={
                'verbose_name': 'Nationality',
                'verbose_name_plural': 'Nationality',
            },
        ),
        migrations.CreateModel(
            name='PartyToBill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('party_to_bill', models.CharField(null=True, max_length=50, blank=True)),
            ],
            options={
                'verbose_name': 'Party to Pay Bill',
                'verbose_name_plural': 'Party to Pay Bill',
            },
        ),
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('patient_no', models.IntegerField(null=True, blank=True, unique=True)),
                ('patient_last_name', models.CharField(null=True, max_length=100, blank=True)),
                ('patient_first_name', models.CharField(null=True, max_length=100, blank=True)),
                ('patient_middle_name', models.CharField(null=True, max_length=100, blank=True)),
                ('patient_birthdate', models.DateField()),
                ('patient_age', models.IntegerField()),
                ('patient_home_add', models.TextField(null=True, blank=True)),
                ('patient_occupation', models.CharField(null=True, max_length=100, blank=True)),
                ('patient_emloyer', models.CharField(null=True, max_length=100, blank=True)),
                ('patient_office_add', models.TextField(null=True, blank=True)),
                ('patient_father_name', models.CharField(null=True, max_length=100, blank=True)),
                ('patient_spouse_name', models.CharField(null=True, max_length=100, blank=True)),
                ('admission_date', models.DateTimeField(auto_now_add=True)),
                ('ward', models.CharField(null=True, max_length=50, blank=True)),
                ('room_no', models.IntegerField(null=True, blank=True)),
                ('bed_no', models.IntegerField(null=True, blank=True)),
                ('patient_informant_name', models.CharField(null=True, max_length=100, blank=True)),
                ('patient_informant_relationship', models.CharField(null=True, max_length=100)),
                ('discharge_date', models.DateTimeField(null=True, blank=True)),
                ('admitting_dxg', models.TextField(null=True, blank=True)),
                ('final_dxg', models.TextField(null=True, blank=True)),
                ('implication', models.TextField(null=True, blank=True)),
                ('code', models.IntegerField(null=True, blank=True)),
                ('slug', models.SlugField(max_length=300, unique=True)),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
            },
        ),
        migrations.CreateModel(
            name='PhysicianInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('dr_last_name', models.CharField(max_length=100)),
                ('dr_first_name', models.CharField(max_length=100)),
                ('dr_middle_initial', models.CharField(max_length=3)),
                ('slug', models.SlugField(max_length=300, unique=True)),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('religion', models.CharField(null=True, max_length=50, blank=True)),
            ],
            options={
                'verbose_name': 'Religion',
                'verbose_name_plural': 'Religion',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('result', models.CharField(null=True, max_length=50, blank=True)),
            ],
            options={
                'verbose_name': 'Result',
                'verbose_name_plural': 'Result',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('service', models.CharField(null=True, max_length=50, blank=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Service',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('doctor', models.ManyToManyField(to='denzo.PhysicianInfo')),
                ('patient', models.ForeignKey(to='denzo.PatientInfo')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Tests',
            },
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='attending_physician',
            field=models.ManyToManyField(related_name='attending_physician2', to='denzo.PhysicianInfo'),
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='physician',
            field=models.ManyToManyField(related_name='attending_phycisian1', to='denzo.PhysicianInfo'),
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='resident_in_charge',
            field=models.ManyToManyField(related_name='resident_physician', to='denzo.PhysicianInfo'),
        ),
    ]
