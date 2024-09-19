from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


UserProfile = get_user_model()
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            return None

        try:
            if '@' in username:
                user = UserProfile.objects.get(email=username)
            else:
                user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
