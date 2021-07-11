from django.db import models

class Patient(models.Model):
	def __str__(self) -> str:
		return super().__str__()
	
	# static fields (manditory)
	first_name = models.CharField(max_length=30, verbose_name="First Name")
	last_name = models.CharField(max_length=30, verbose_name="Last Name")
	dob = models.DateField(verbose_name="Date of Birth")
	telnum = models.CharField(max_length=10, verbose_name="Telephone Number")
	email = models.CharField(max_length=255, verbose_name="Email Address")
	
	# variable fields
	medneed = models.CharField(max_length=255, verbose_name="Medical Needs")
	resolve = models.BooleanField()

class Doctor(models.Model):
	def __str__(self) -> str:
		return super().__str__()
	
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	telnum = models.CharField(max_length=10, verbose_name="Telephone Number")
	email = models.CharField(max_length=255, verbose_name="Email Address")
	
class Appt(models.Model):
	def __str__(self) -> str:
		return super().__str__()

	dateappt = models.DateTimeField(verbose_name="Date of Appointment")
	location = models.CharField(max_length=255, verbose_name="Location")
	lastapp = models.DateField(verbose_name="Date of last appointment.")
	toolsneeded = models.CharField(max_length=255)
	procedure = models.CharField(max_length=255)
	patienttools = models.CharField(max_length=255)