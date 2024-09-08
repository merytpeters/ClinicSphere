from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from myapp.models import Patient
from patientportal.models import UserProfile


@receiver(post_save, sender=Patient)
def create_patient_user(sender, instance, created, **kwargs):
    print("Signal triggered")
    if created:
        try:
            user = User.objects.create(
                username=instance.email,
                email=instance.email,
                first_name=instance.first_name,
                last_name=instance.last_name
            )
            # Set password to be created later
            user.set_unusable_password
            user.save()

            UserProfile.objects.create(user=user, is_patient=True)
            print(f"User Profile for {user.username} created successfully.")
        except Exception as e:
            print(f"Error creating user profile")
         
