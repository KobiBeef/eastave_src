from django.contrib import admin
from . import models

# Register your models here.
class PatientNameAdmin(admin.ModelAdmin):
	list_display = ("pt_last_name", "pt_first_name", "pt_middle_name")
	prepopulated_fields = {"slug": ("pt_last_name", "pt_first_name", "pt_middle_name"),}

class PhysicianNameAdmin(admin.ModelAdmin):
	list_display = ("dr_last_name", "dr_first_name", "dr_middle_initial")
	prepopulated_fields = {"slug": ("dr_last_name", "dr_first_name", "dr_middle_initial")}

class TestAdmin(admin.ModelAdmin):
	list_display = ("patient",)

admin.site.register(models.PatientName, PatientNameAdmin)
admin.site.register(models.PhysicianName, PhysicianNameAdmin)
admin.site.register(models.Test, TestAdmin)