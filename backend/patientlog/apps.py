from django.apps import AppConfig


class PatientlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # tells you the default models to use
    name = 'patientlog'
