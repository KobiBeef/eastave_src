# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denzo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientname',
            old_name='pt_age',
            new_name='patient_age',
        ),
        migrations.RenameField(
            model_name='patientname',
            old_name='pt_birthdate',
            new_name='patient_birthdate',
        ),
        migrations.RenameField(
            model_name='patientname',
            old_name='pt_emloyer',
            new_name='patient_informant_relationship',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='encoder_first_name',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='encoder_last_name',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='encoder_middiel_initial',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='mode_payment',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_class',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_disposition',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_first_name',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_fthr_first_name',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_fthr_last_name',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_home_add',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_informant_first_name',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_informant_last_name',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_informant_relationship',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_last_name',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_membership',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_middle_name',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_mthr_first_name',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_mthr_last_name',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_nationality',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_no',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_occupation',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_office_add',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_religion',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_result',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_sex',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_spouse_first_name',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_spouse_last_name',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_spouse_middle_name',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='pt_status',
        ),
        migrations.RemoveField(
            model_name='patientname',
            name='service',
        ),
        migrations.AddField(
            model_name='patientname',
            name='discharge_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patientname',
            name='patient_emloyer',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patientname',
            name='patient_father_name',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patientname',
            name='patient_first_name',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patientname',
            name='patient_home_add',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patientname',
            name='patient_informant_name',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patientname',
            name='patient_last_name',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patientname',
            name='patient_middle_name',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patientname',
            name='patient_no',
            field=models.IntegerField(null=True, blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='patientname',
            name='patient_occupation',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patientname',
            name='patient_office_add',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patientname',
            name='patient_spouse_name',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='patientname',
            name='admitting_dxg',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientname',
            name='bed_no',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientname',
            name='code',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientname',
            name='final_dxg',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientname',
            name='implication',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientname',
            name='room_no',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientname',
            name='ward',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
    ]
