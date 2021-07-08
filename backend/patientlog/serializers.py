from django.db.models import fields
from rest_framework import serializers
from .models import Patient, Doctor

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
		]
		extra_kwargs = [
			"allergies",
		]

class DoctorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Doctor
		fields = [
			"pk",
			"first_name", 
			"last_name"
		]