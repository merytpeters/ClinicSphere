from patientportal.models import *
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user',
                  'is_patient',
                  'profile_picture']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PatientFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientFolder
        fields = '__all__'