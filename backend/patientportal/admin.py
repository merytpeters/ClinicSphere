from django.contrib import admin
from patientportal.models import UserProfile, PatientFolder

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(PatientFolder)