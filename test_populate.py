import os
import json

def populate():
	jsonfile = open('jan_ward.json').read()
	info = json.loads(jsonfile)

	for item in info:
		add_item_new(
			item['DATE OF ADMISSION'], 
			item['HOSPITAL NUMBER'], 
			item['NAME'], 
			item['AGE'], 
			item['GENDER'], 
			item['CATEGORY'], 
			item['ICD-10'], 
			item['ADMITTING DIAGNOSIS'], 
			item['FINAL DIAGNOSIS'], 
			item['DISPOSITION'], 
			item['DATE OF DISCHARGE'], 
			item['HOSPITAL STAY IN DAYS']
			)
		
		# print (item['DATE OF ADMISSION'], item['GENDER'])

	# jsonfile = open('test_gender.json').read()
	# info = json.loads(jsonfile)

	# for item in info:
	# 	add_item(item['Gender'])

	# for i in Test.objets.all():
	# 	print

	# for item in info:
	# 	for itm in item['Gender']:
	# 		item['Gender'] = itm.strip()
	
	# print (item['Gender'])

# def add_item_new(name, gender):
# 	i = PatientInfo2.objects.get_or_create(name=name, gender=gender)
# 	return i

def add_item_new(date_of_admission, hospital_number, name, age, gender, category, icd_10, admitting_dxg, final_dxg, disposition, date_of_discharge, hospital_stay_in_days):
	i = PatientInfo2.objects.get_or_create(
		date_of_admission=date_of_admission, 
		hospital_number=hospital_number, 
		name=name, 
		age=age, 
		gender=gender, 
		category=category, 
		icd_10=icd_10, 
		admitting_dxg=admitting_dxg, 
		final_dxg=final_dxg, 
		disposition=disposition, 
		date_of_discharge=date_of_discharge, 
		hospital_stay_in_days=hospital_stay_in_days
		)
	return i

# def add_item(test_gender):
# 	i = Test.objects.get_or_create(test_gender=test_gender)
# 	return i

if __name__ == '__main__':
	print ("Starting Population of test_name")
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eastave.settings')
	from denzo.models import Test, PatientInfo2
	populate()

# hard populate
# populate()