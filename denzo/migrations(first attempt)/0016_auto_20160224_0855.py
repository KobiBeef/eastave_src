# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0015_patientdisposition'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('patient_no', models.IntegerField(unique=True, blank=True, null=True)),
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
                ('slug', models.SlugField(unique=True, max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Patients',
                'verbose_name': 'Patient',
            },
        ),
        migrations.RenameModel(
            old_name='PatientBillParty',
            new_name='CivilStatus',
        ),
        migrations.RenameModel(
            old_name='PatientMembership',
            new_name='Classification',
        ),
        migrations.RenameModel(
            old_name='PatientClassification',
            new_name='Disposition',
        ),
        migrations.RenameModel(
            old_name='PatientGender',
            new_name='Gender',
        ),
        migrations.RenameModel(
            old_name='PatientCivilStatus',
            new_name='Membership',
        ),
        migrations.RenameModel(
            old_name='PatientDisposition',
            new_name='Nationality',
        ),
        migrations.RenameModel(
            old_name='PatientService',
            new_name='PartyToBill',
        ),
        migrations.RenameModel(
            old_name='PhysicianName',
            new_name='PhysicianInfo',
        ),
        migrations.RenameModel(
            old_name='PatientNationality',
            new_name='Religion',
        ),
        migrations.RenameModel(
            old_name='PatientResult',
            new_name='Result',
        ),
        migrations.RenameModel(
            old_name='PatientReligion',
            new_name='Service',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='attending_physician',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='physician',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='resident_in_charge',
        ),
        migrations.AlterModelOptions(
            name='civilstatus',
            options={'verbose_name_plural': 'Civil Status', 'verbose_name': 'Civil Status'},
        ),
        migrations.AlterModelOptions(
            name='classification',
            options={},
        ),
        migrations.AlterModelOptions(
            name='disposition',
            options={'verbose_name_plural': 'Disposition', 'verbose_name': 'Disposition'},
        ),
        migrations.AlterModelOptions(
            name='membership',
            options={'verbose_name_plural': 'Membership', 'verbose_name': 'Membership'},
        ),
        migrations.AlterModelOptions(
            name='nationality',
            options={'verbose_name_plural': 'Nationality', 'verbose_name': 'Nationality'},
        ),
        migrations.AlterModelOptions(
            name='partytobill',
            options={'verbose_name_plural': 'Party to Pay Bill', 'verbose_name': 'Party to Pay Bill'},
        ),
        migrations.AlterModelOptions(
            name='religion',
            options={'verbose_name_plural': 'Religion', 'verbose_name': 'Religion'},
        ),
        migrations.AlterModelOptions(
            name='result',
            options={'verbose_name_plural': 'Result', 'verbose_name': 'Result'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name_plural': 'Service', 'verbose_name': 'Service'},
        ),
        migrations.RenameField(
            model_name='civilstatus',
            old_name='patient_bill_party',
            new_name='civil_status',
        ),
        migrations.RenameField(
            model_name='classification',
            old_name='patient_membership',
            new_name='payment_class',
        ),
        migrations.RenameField(
            model_name='disposition',
            old_name='patient_class',
            new_name='disposition',
        ),
        migrations.RenameField(
            model_name='gender',
            old_name='patient_gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='patient_civil_status',
            new_name='membership',
        ),
        migrations.RenameField(
            model_name='nationality',
            old_name='patient_disposition',
            new_name='nationality',
        ),
        migrations.RenameField(
            model_name='partytobill',
            old_name='patient_service',
            new_name='party_to_bill',
        ),
        migrations.RenameField(
            model_name='religion',
            old_name='patient_nationality',
            new_name='religion',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='patient_result',
            new_name='result',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='patient_religion',
            new_name='service',
        ),
        migrations.AlterField(
            model_name='test',
            name='patient',
            field=models.ForeignKey(to='denzo.PatientInfo'),
        ),
        migrations.DeleteModel(
            name='PatientName',
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
