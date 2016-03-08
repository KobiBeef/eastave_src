from django.contrib import admin
from . import models

# Register your models here.
class PatientInfoAdmin(admin.ModelAdmin):
	list_display = ("patient_last_name", "patient_first_name", "patient_middle_name")
	prepopulated_fields = {"slug": ("patient_last_name", "patient_first_name", "patient_middle_name"),}

# FROM CODE ENTREPRENUER
# class PatientNameAdmin(admin.ModelAdmin):
	# list_display = ["patient_last_name", "patient_first_name", "patient_middle_name"]
	# prepopulated_fields = {"slug": ("patient_last_name", "patient_first_name", "patient_middle_name"),}
	# class Meta:
	# 	model = PatientName

class PhysicianInfoAdmin(admin.ModelAdmin):
	list_display = ("dr_last_name", "dr_first_name", "dr_middle_initial")
	prepopulated_fields = {"slug": ("dr_last_name", "dr_first_name", "dr_middle_initial")}

class ServiceAdmin(admin.ModelAdmin):
	list_display = ("service",)

class GenderAdmin(admin.ModelAdmin):
	list_display = ("gender",)

class CivilStatusAdmin(admin.ModelAdmin):
	list_display = ("civil_status",)

class NationalityAdmin(admin.ModelAdmin):
	list_display = ("nationality",)

class ReligionAdmin(admin.ModelAdmin):
	list_display = ("religion", )

class MembershipAdmin(admin.ModelAdmin):
	list_display = ("membership", )

class PartyToBillAdmin(admin.ModelAdmin):
	list_display = ("party_to_bill", )

class EncoderAdmin(admin.ModelAdmin):
	list_display = ("encoder_last_name", "encoder_first_name",)

class ClassificationAdmin(admin.ModelAdmin):
	list_display = ("payment_class",)

class ResultAdmin(admin.ModelAdmin):
	list_display = ("result",)

class DispositionAdmin(admin.ModelAdmin):
	list_display = ("disposition",)

class PatientInfo2Admin(admin.ModelAdmin):
	list_display = ("date_of_admission", "hospital_number", "name",)

class TestAdmin(admin.ModelAdmin):
	list_display = ("test_gender",)
	

# FROM CODE ENTREPRENUER
# class PhysicianNameAdmin(admin.ModelAdmin):
	# list_display = ["dr_last_name", "dr_first_name", "dr_middle_initial"]
	# prepopulated_fields = {"slug": ("dr_last_name", "dr_first_name", "dr_middle_initial")}
	# class Meta:
	# 	model = PhysicianName

admin.site.register(models.PatientInfo, PatientInfoAdmin)
admin.site.register(models.PhysicianInfo, PhysicianInfoAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Gender, GenderAdmin)
admin.site.register(models.CivilStatus, CivilStatusAdmin)
admin.site.register(models.Nationality, NationalityAdmin)
admin.site.register(models.Religion, ReligionAdmin)
admin.site.register(models.Membership, MembershipAdmin)
admin.site.register(models.PartyToBill, PartyToBillAdmin)
admin.site.register(models.Encoder, EncoderAdmin)
admin.site.register(models.Classification, ClassificationAdmin)
admin.site.register(models.Result, ResultAdmin)
admin.site.register(models.Disposition, DispositionAdmin)
admin.site.register(models.PatientInfo2, PatientInfo2Admin)
admin.site.register(models.Test, TestAdmin)