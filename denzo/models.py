from django.db import models
import uuid

# Create your models here.
# pilot database for patient

# Creating/testing a unique patient/hospital number for patient/s
# def rand_key(size):
	# python 3 does not support string.letters so use string ascii_letters
    # return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(size)])

class PhysicianName(models.Model):
	# DOCTOR NAME:
	dr_last_name = models.CharField(max_length=100)
	dr_first_name = models.CharField(max_length=100)
	dr_middle_initial = models.CharField(max_length=3)
	# FOR UNIQUENESS OF PHYSICIAN NAME
	# FOR DOCTOR UNIQUENESS USE SLUG AS OF NOW
	slug = models.SlugField(max_length=300, unique=True)
	# for unique doctor_no
	# FOR FUTURE USE of doctor_no
	# doctor_no = models.UUIDField(default=uuid, unique=True)
	# LETS TRY ONE WAY CONNECTION: One Doctor:Many Patient/s
	# then try to connet to doctor through patient/s
	# patient = models.ForeignKey(PatientName, null=True)

	def __str__(self):
		return self.dr_last_name + ", " + self.dr_first_name + " " + self.dr_middle_initial+"."


	class Meta:
		verbose_name = "Doctor"
		verbose_name_plural = "Doctors"

class PatientName(models.Model):
	#####################################################
	# First part of form                                #
	#####################################################
	# BASIC PATINT INFO:
	pt_no = models.IntegerField(unique=True)
	pt_last_name = models.CharField(max_length=100)
	pt_first_name = models.CharField(max_length=100)
	pt_middle_name = models.CharField(max_length=100)

	# THIS IS THE WARD must have a class of its own
	service = models.CharField(max_length=100)
	
	# TESTING PHYSICIAN M2M field
	physician = models.ManyToManyField(PhysicianName, related_name='attending_phycisian1')
	
	pt_birthdate = models.DateField()
	pt_age = models.IntegerField()
	pt_sex = models.CharField(max_length=20)
	pt_status = models.CharField(max_length=15)
	pt_nationality = models.CharField(max_length=20)
	pt_religion = models.CharField(max_length=20)
	pt_home_add = models.TextField()
	pt_office_add = models.TextField(null=True)
	pt_occupation = models.CharField(max_length=100, null=True)
	pt_emloyer = models.CharField(max_length=100, null=True)
	pt_membership = models.CharField(max_length=50, null=True)

	#####################################################
	# Second part of form                               #
	#####################################################
	# PT_PARENTS
	pt_fthr_last_name = models.CharField(max_length=100)
	pt_fthr_first_name = models.CharField(max_length=100)
	pt_mthr_last_name = models.CharField(max_length=100)
	pt_mthr_first_name = models.CharField(max_length=100)
	# PT_SPOUSE IF pt.status == married:
	pt_spouse_last_name = models.CharField(max_length=100)
	pt_spouse_first_name = models.CharField(max_length=100)
	pt_spouse_middle_name = models.CharField(max_length=100)

	#####################################################
	# Third part of form                                #
	#####################################################
	# PT PARTY TO PAY BILLS: CHECKBOX appearance if in form
	# check wether you can check all choices
	# as of now we put it in a models.CharField()
	mode_payment = models.CharField(max_length=100)

	# will refine this variable admitting_dxg to register all possible diagnosis
	# thinking of regular expression to specify the diagnosises
	admitting_dxg = models.TextField()

	#####################################################
	# Fourth part of form                               #
	#####################################################
	# ADMISSION INFO:
	admission_date = models.DateTimeField(auto_now_add=True)
	ward = models.CharField(max_length=50)
	room_no = models.IntegerField(null=True)
	bed_no = models.IntegerField(null=True)
	
	# variable encoder_name SHOULD HAVE A CLASS/MODEL OF ITS OWN
	encoder_last_name = models.CharField(max_length=100)
	encoder_first_name = models.CharField(max_length=100)
	encoder_middiel_initial = models.CharField(max_length=5)

	# pt_clas: CHECKBOX appearance if in form
	# will have a class of its own?
	pt_class = models.CharField(max_length=20)

	pt_informant_first_name = models.CharField(max_length=100, null=True)
	pt_informant_last_name = models.CharField(max_length=100, null=True)
	pt_informant_relationship = models.CharField(max_length=100, null=True)

	#####################################################
	# Fith part of form                                 #
	#####################################################
	# DIAGNOSISES
	# check fourth part of form for variable admitting_dxg
	# admitting_dxg
	# will refine this variable final_dxg to register all possible diagnosis
	# thinking of regular expression to specify the diagnosises
	final_dxg = models.TextField()

	# will also refine this variable implication to register all possible implications
	# thinking of regular expression to specify/divide/slash the implications
	implication = models.TextField()

	# i dont Know what this is for
	code = models.IntegerField(null=True)

	#####################################################
	# Sixth part of form                                #
	#####################################################
	# RESULTS: CHECKBOX appearance if in form as of now put in model.CharField()
	pt_result = models.CharField(max_length=100)
	
	# DISPOSITION: CHECKBOX appearance if in form as of now put in model.CharField()
	pt_disposition = models.CharField(max_length=100)

	#####################################################
	# Seventh part of form                              #
	#####################################################
	resident_in_charge = models.ManyToManyField(PhysicianName, related_name='resident_physician')
	attending_physician = models.ManyToManyField(PhysicianName, related_name='attending_physician2')

	# FOR UNIQUENESS OF PATIENT NAME
	# FOR PATIENT UNIQUENES and url mapping USE SLUG FOR NOW
	slug = models.SlugField(max_length=300, unique=True)
	# OPTION 2: UUID field
	# for unique patient_no
	# FOR FUTURE USE of patient_no
	# patient_no = models.UUIDField(default=uuid.uuid4, editable=False)

	# doctor = models.ForeignKey(DoctorName)
	# hospital_no = models.IntegerField(null=True)

	# identifier = models.CharField(max_length=16, unique=True)

	# OPTION 1: DID NOT WORK
	# def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
	# 	if self.identifier is None or len(self.identifier) == 0:
	# 		self.identifier = rand_key(16)
	# 	super(PatientName, self).save(self, force_insert, force_update, using, update_fields)

	def __str__(self):
		return self.pt_last_name + ", " + self.pt_first_name + " " + self.pt_middle_name+". "

	class Meta:
		verbose_name = "Patient"
		verbose_name_plural = "Patients"



# class to take patient and doctor
class Test(models.Model):
	doctor = models.ManyToManyField(PhysicianName)
	patient = models.ForeignKey(PatientName)

	def __str__(self):
		return self.patient.pt_last_name

	class Meta:
		verbose_name = "Test"
		verbose_name_plural = "Tests"

# FOR FUTURE USE
# class Ward(model.Model):
# 	# service = model.CharField(max_length=300, unique=True)

# class Sex(model.Model):
# 	sex = model.CharField()