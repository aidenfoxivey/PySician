from django.db import models

class Patient(models.Model):
	# let's call it something more pleasing
	# kinda shitty implementation, but threw error on self.title
	def __str__(self):
		return "Patient"

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	dob = models.DateField()
	# can pull age out of there
	telnum = models.CharField(max_length=10)
	# international standard xxx-xxx-xxxx (10 char)
	email = models.CharField(max_length=255)
	allergies=models.CharField(max_length=255, null=True, blank=True)

class Doctor(models.Model):
	def __str__(self):
		return "Doctor"
	
	first_name = models.CharField(max_length=30, null=True)
	last_name = models.CharField(max_length=30, null=True)