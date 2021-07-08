from django.urls import path
from . import views

'''
function as 'in-points' for where we can make CRUD requests
'''

urlpatterns = [
	path("doctors/", views.DoctorList.as_view()),
	path("doctors/<int:pk>", views.DoctorDetail.as_view()),
	path("patients/", views.PatientList.as_view()),
	path("patients/<int:pk>", views.PatientDetail.as_view()),
]