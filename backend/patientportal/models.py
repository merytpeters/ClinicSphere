from django.db import models
from django.contrib.auth.models import User
from myapp.models import Patient

# Create your models here.


class UserProfile(models.Model):
    """Individual user profiles of patient to access
      their own record withh read only access"""
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_patient = models.BooleanField(default=True)
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    

class PatientFolder(Patient):
    """Patient Folder for storing and view all medical history"""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_profile')
    # name = models.CharField(max_length=100)
    age = models.IntegerField()
    medicalhistory = models.TextField()

    def __str__(self):
        return self.name