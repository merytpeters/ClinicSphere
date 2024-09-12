from django.db import models
from myapp.models import Patient

# Create your models here.


class UserProfile(models.Model):
    """Individual user profiles of patient to access
      their own record withh read only access"""
    user = models.OneToOneField(
        Patient,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_patient = models.BooleanField(default=True)
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    