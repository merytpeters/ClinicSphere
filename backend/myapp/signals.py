from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from myapp.models import Patient, UserProfile


@receiver(post_save, sender=Patient)
def create_patient_user(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create(
            username=instance.email,
            email=instance.email
        )
        # Set password to be created later
        user.set_unusable_password()
        user.save()
        UserProfile.objects.create(user=user, is_patient=True)
