from django.shortcuts import render
from rest_framework import generics
from .models import Patient,Doctor
from .serializers import PatientSerializer,DoctorSerializer
from django.http import HttpResponse
import datetime
# generic views -- core of CRUD apps
# view -- takes request, returns response 
'''
request -- can come from frontend or viewer
response -- redirect, 404 error, XML doc.
'''

# no longer need to write a full list of CRUD functions
# generics let us write this with less

class PatientList(generics.ListCreateAPIView):
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer
	# creates the get and post function

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer

class DoctorList(generics.ListCreateAPIView):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer