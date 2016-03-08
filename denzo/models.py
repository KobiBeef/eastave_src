from django.db import models
import uuid

# Create your models here.
# pilot database for patient

# Creating/testing a unique patient/hospital number for patient/s
# def rand_key(size):
	# python 3 does not support string.letters so use string ascii_letters
    # return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(size)])

class PhysicianInfo(models.Model):
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
		verbose_name = "Physician Info"
		verbose_name_plural = "Physician Info"

###################
# PATIENT SERVICE #
###################
class Service(models.Model):
	# change variable name to service
	service = models.CharField(max_length=50, blank=True, null=True)
	# patient_service = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.service

	class Meta:
		verbose_name = "Service"
		verbose_name_plural = "Service"

##################
# PATIENT GENDER #
##################
class Gender(models.Model):
	# change variable name to gender
	gender = models.CharField(max_length=10, blank=True, null=True)

	def __str__(self):
		return self.gender

	class Meta:
		verbose_name = "Gender"
		verbose_name_plural = "Gender"

########################
# PATIENT CIVIL STATUS #
########################
class CivilStatus(models.Model):
	# change variable name to civil_status
	civil_status = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.civil_status

	class Meta:
		verbose_name = "Civil Status"
		verbose_name_plural = "Civil Status"

########################
# PATIENT NATIONALITY  #
########################
class Nationality(models.Model):
	# change variable name to nationality
	nationality = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.nationality

	class Meta:
		verbose_name = "Nationality"
		verbose_name_plural = "Nationality"

####################
# PATIENT RELIGION #
####################
class Religion(models.Model):
	# change variable name to religion
	religion = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.religion

	class Meta:
		verbose_name = "Religion"
		verbose_name_plural = "Religion"

######################
# PATIENT MEMBERSHIP #
######################
class Membership(models.Model):
	# change variable name to membership
	membership = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.membership

	class Meta:
		verbose_name = "Membership"
		verbose_name_plural = "Membership"

########################
# PATIENT BILL PARTY #
########################
class PartyToBill(models.Model):
	# change variable name to party_to_bill
	party_to_bill = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.party_to_bill

	class Meta:
		verbose_name = "Party to Pay Bill"
		verbose_name_plural = "Party to Pay Bill"

###########
# ENCODER #
###########
class Encoder(models.Model):
	encoder_last_name = models.CharField(max_length=50, blank=True, null=True)
	encoder_first_name = models.CharField(max_length=50, blank=True, null=True)
	encoder_middle_initial = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.encoder_last_name + ", " + self.encoder_first_name + " " + self.encoder_middle_initial

	class Meta:
		verbose_name = "Encoder"
		verbose_name_plural = "Encoders"

##########################
# PATIENT CLASSIFICATION #
##########################
class Classification(models.Model):
	# change variable name to payment_class
	payment_class = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.payment_class

##################
# PATIENT RESULT #
##################
class Result(models.Model):
	# change variable name to result
	result = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.result

	class Meta:
		verbose_name = "Result"
		verbose_name_plural = "Result"

#######################
# PATIENT DISPOSITION #
#######################
class Disposition(models.Model):
	# change variable name to disposition
	disposition = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.disposition

	class Meta:
		verbose_name = "Disposition"
		verbose_name_plural = "Disposition"

class PatientInfo(models.Model):
	#####################################################
	# First part of form                                #
	#####################################################
	# BASIC PATINT INFO:
	patient_no = models.IntegerField(unique=True, blank=True, null=True)
	patient_last_name = models.CharField(max_length=100, blank=True, null=True)
	patient_first_name = models.CharField(max_length=100, blank=True, null=True)
	patient_middle_name = models.CharField(max_length=100, blank=True, null=True)

	# THIS IS THE WARD must have a class of its own
	################################################
	# WILL BE REMOVED must have a class of its own #
	################################################
	# service = models.CharField(max_length=100)
	patient_service = models.ForeignKey(Service, blank=True, null=True)
	
	# TESTING PHYSICIAN M2M field
	attending_physician = models.ManyToManyField(PhysicianInfo, related_name='attending_phycisian1', blank=True)
	patient_birthdate = models.DateField(blank=True, null=True)
	
	################################################
	# WILL BE REMOVED must have a class of its own #
	################################################
	patient_gender = models.ForeignKey(Gender, blank=True, null=True)

	patient_age = models.IntegerField(blank=True, null=True)
	# THIS SHOULD BE A RADIO BUTTON FIELD
	# MALE, FEMALE
	
	
	# THIS SHOULD BE A RADIO BUTTON FIELD
	# SINGLE, MARRIED, WIDOW
	################################################
	# WILL BE REMOVED must have a class of its own #
	################################################
	patient_civil_status = models.ForeignKey(CivilStatus, blank=True, null=True)

	# CONSIDERING THIS TO BE A RADIO FIELD
	################################################
	# WILL BE REMOVED must have a class of its own #
	################################################
	patient_nationality = models.ForeignKey(Nationality, blank=True, null=True)

	################################################
	# WILL BE REMOVED must have a class of its own #
	################################################
	patient_religion = models.ForeignKey(Religion, blank=True, null=True)

	patient_home_add = models.TextField(blank=True, null=True)
	patient_occupation = models.CharField(max_length=100, blank=True, null=True)
	patient_emloyer = models.CharField(max_length=100, blank=True, null=True)
	patient_office_add = models.TextField(blank=True, null=True)
	# employer

	################################################
	# WILL BE REMOVED must have a class of its own #
	################################################
	# patient_membership = models.CharField(max_length=50, null=True)
	patient_membership = models.ForeignKey(Membership, blank=True, null=True)

	#####################################################
	# Second part of form                               #
	#####################################################
	# patient_PARENTS
	# reduce to one CharField
	# no need to separate names
	# patient_fthr_last_name = models.CharField(max_length=100)
	# patient_fthr_first_name = models.CharField(max_length=100)
	# patient_mthr_last_name = models.CharField(max_length=100)
	# patient_mthr_first_name = models.CharField(max_length=100)
	patient_father_name = models.CharField(max_length=100, blank=True, null=True)
	patient_mother_name = models.CharField(max_length=100, blank=True, null=True)
	# patient_SPOUSE IF patient.status == married:
	# reduce to one CharField
	# no need to separate names
	# patient_spouse_last_name = models.CharField(max_length=100)
	# patient_spouse_first_name = models.CharField(max_length=100)
	# patient_spouse_middle_name = models.CharField(max_length=100)
	patient_spouse_name = models.CharField(max_length=100, blank=True, null=True)

	#####################################################
	# Third part of form                                #
	#####################################################
	# patient PARTY TO PAY BILLS: CHECKBOX OR RADIO FIELD appearance if in form
	# check wether you can check all choices
	# as of now we put it in a models.CharField()
	party_to_bill = models.ForeignKey(PartyToBill, blank=True, null=True)

	# will refine this variable admitting_dxg to register all possible diagnosis
	# thinking of regular expression to specify the diagnosises
	admitting_dxg = models.TextField(blank=True, null=True)
	
	#####################################################
	# Fourth part of form                               #
	#####################################################
	# ADMISSION INFO:
	admission_date = models.DateTimeField(blank=True, null=True)
	# THIS SHOULD BE A RADIO BUTTON FIELD
	ward = models.CharField(max_length=50, blank=True, null=True)
	room_no = models.IntegerField(blank=True, null=True)
	bed_no = models.IntegerField(blank=True, null=True)
	rate = models.IntegerField(blank=True, null=True)
	
	# variable encoder_name SHOULD HAVE A CLASS/MODEL OF ITS OWN
	################################################
	# WILL BE REMOVED must have a class of its own #
	################################################
	# encoder_last_name = models.CharField(max_length=100)
	# encoder_first_name = models.CharField(max_length=100)
	# encoder_middiel_initial = models.CharField(max_length=5)
	patient_info_encoder = models.ForeignKey(Encoder, blank=True, null=True)

	
	################################################
	# WILL BE REMOVED must have a class of its own #
	################################################
	# mode_payment = models.CharField(max_length=100)
	patient_classification = models.ForeignKey(Classification, blank=True, null=True)

	# reduce to one CharField
	# no need to separate names
	# patient_informant_first_name = models.CharField(max_length=100, null=True)
	# patient_informant_last_name = models.CharField(max_length=100, null=True)
	patient_informant_name = models.CharField(max_length=100, blank=True, null=True)
	patient_informant_relationship = models.CharField(max_length=100, blank=True, null=True)

	discharge_date = models.DateTimeField(blank=True, null=True)
	
	###########################
	# not sure about this one #
	###########################
	discharge_physician = models.ForeignKey(PhysicianInfo, blank=True, null=True, related_name='discharge_physician')

	#####################################################
	# Fith part of form                                 #
	#####################################################
	# DIAGNOSISES
	# check fourth part of form for variable admitting_dxg
	# admitting_dxg
	# will refine this variable final_dxg to register all possible diagnosis
	# thinking of regular expression to specify the diagnosises
	final_dxg = models.TextField(blank=True, null=True)

	# will also refine this variable implication to register all possible implications
	# thinking of regular expression to specify/divide/slash the implications
	implication = models.TextField(blank=True, null=True)

	# i dont Know what this is for
	code = models.IntegerField(blank=True, null=True)

	#####################################################
	# Sixth part of form                                #
	#####################################################
	# RESULTS: CHECKBOX appearance if in form as of now put in model.CharField()
	################################################
	# WILL BE REMOVED must have a class of its own #
	################################################
	patient_result = models.ForeignKey(Result, blank=True, null=True)
	
	################################################
	# WILL BE REMOVED must have a class of its own #
	################################################
	# DISPOSITION: CHECKBOX appearance if in form as of now put in model.CharField()
	# patient_disposition = models.CharField(max_length=100)
	patient_disposition = models.ForeignKey(Disposition, blank=True, null=True)

	#####################################################
	# Seventh part of form                              #
	#####################################################
	resident_in_charge = models.ManyToManyField(PhysicianInfo, related_name='resident_physician', blank=True)
	physician = models.ManyToManyField(PhysicianInfo, related_name='attending_physician2', blank=True)

	# FOR UNIQUENESS OF PATIENT NAME
	# FOR PATIENT UNIQUENES and url mapping USE SLUG FOR NOW
	slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
	# OpatientION 2: UUID field
	# for unique patient_no
	# FOR FUTURE USE of patient_no
	# patient_no = models.UUIDField(default=uuid.uuid4, editable=False)

	# doctor = models.ForeignKey(DoctorName)
	# hospital_no = models.IntegerField(null=True)

	# identifier = models.CharField(max_length=16, unique=True)

	# OpatientION 1: DID NOT WORK
	# def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
	# 	if self.identifier is None or len(self.identifier) == 0:
	# 		self.identifier = rand_key(16)
	# 	super(PatientName, self).save(self, force_insert, force_update, using, update_fields)

	def __str__(self):
		return self.patient_last_name + ", " + self.patient_first_name + " " + self.patient_middle_name+". "

	class Meta:
		verbose_name = "Patient Info"
		verbose_name_plural = "Patient Info"

class PatientInfo2(models.Model):
	date_of_admission = models.DateField(blank=True, null=True)
	hospital_number = models.IntegerField(blank=True, null=True)
	name = models.CharField(max_length=50, blank=True, null=True)
	age = models.IntegerField(blank=True, null=True)
	gender = models.CharField(max_length=50, blank=True, null=True)
	category = models.CharField(max_length=50, blank=True, null=True)
	icd_10 = models.CharField(max_length=50, blank=True, null=True)
	admitting_dxg = models.TextField(blank=True, null=True)
	final_dxg = models.TextField(blank=True, null=True)
	disposition = models.CharField(max_length=50, blank=True, null=True)
	date_of_discharge = models.DateField(blank=True, null=True)
	hospital_stay_in_days = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Patient Info 2"
		verbose_name_plural = "Patient Info 2"

# class to take patient and doctor
class Test(models.Model):
	# doctor = models.ManyToManyField(PhysicianInfo)
	# patient = models.ForeignKey(PatientInfo)
	# test_gender = models.ForeignKey(Gender, max_length=10, blank=True, null=True)
	# tried to conver foreign key to charfield.. didn't work
	test_gender = models.CharField(max_length=10, blank=True, null=True)

	def __str__(self):
		return self.test_gender.gender
		# return str(self.timestap)
		# return self.patient.patient_last_name

	class Meta:
		verbose_name = "Test"
		verbose_name_plural = "Tests"

# FOR FUTURE USE
# class Ward(model.Model):
# 	# service = model.CharField(max_length=300, unique=True)

