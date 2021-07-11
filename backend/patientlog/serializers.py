from django.db.models import fields
from rest_framework import serializers
from .models import Patient, Doctor, Appt

class PatientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		# fields that we can expect to see come in
		fields = [
			"pk", # primary key here 
			"first_name", 
			"last_name",
			"dob",
			"telnum",
			"email",
			"medneed",
			"resolve",
		]
		#extra_kwargs = [
		#	"allergies",
		#]

## extra is for not strictly necessary items, those that aren't required

class DoctorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Doctor
		fields = [
			"pk",
			"first_name", 
			"last_name",
			"telnum",
			"email",
		]

class ApptSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appt
		fields = [
			'dateappt', 
			'location', 			
			'lastapp',		
			'toolsneeded', 
			'procedure',
			'patienttools',
		]