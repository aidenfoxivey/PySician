from django.urls import path
from django.conf.urls import url
from . import views

'''
function as 'in-points' for where we can make CRUD requests
'''

urlpatterns = [
	path("doctors/", views.DoctorList.as_view()),
	path("doctors/<int:pk>", views.DoctorDetail.as_view()),
	path("patients/", views.PatientList.as_view()),
	path("patients/<int:pk>", views.PatientDetail.as_view()),
	path("appts/", views.ApptList.as_view()),
	path("appts/<int:pk>", views.ApptDetail.as_view()),

]