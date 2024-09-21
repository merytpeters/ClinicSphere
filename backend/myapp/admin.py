from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Departments)
admin.site.register(TemporaryToken)
admin.site.register(Employees)
admin.site.register(Patient)
admin.site.register(Medication)
admin.site.register(Order)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(PrescriptionMedication)
