from django.contrib.auth import authenticate, get_user_model
from patientportal.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for creating an Patient Profile Creation"""
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email')


UserProfile = get_user_model()

class PatientPasswordSetSerializer(serializers.Serializer):
    """Patient Registration"""
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    def validate(self, attrs):
        email = attrs.get('email')

        # Check if email exists
        if not UserProfile.objects.filter(email=email).exists():
            raise serializers.ValidationError("No patient found with this email.")
            
        # Check passwords match
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match")
            
        password = attrs.get('password1', '')
        if len(password) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters!')
        
        return attrs

    def save(self):
        email = self.validated_data['email']
        password = self.validated_data['password1']

        user = UserProfile.objects.get(email=email)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    """Login Serializer for Patient"""
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user is not None and user.is_active:
            return user
        raise serializers.ValidationError('Incorect Login Credentials')