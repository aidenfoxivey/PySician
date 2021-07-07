from django.contrib import admin

from .models import Patient
from .models import Doctor

# Register created models.
admin.site.register(Patient)
admin.site.register(Doctor)