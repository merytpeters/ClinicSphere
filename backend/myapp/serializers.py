from django.contrib.auth import authenticate
from myapp.models import *
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer for creating an employee, including User creation"""
    class Meta:
        model = Employees
        fields = ('id', 'username', 'email')

class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    """Employee Registration"""
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Employees
        fields = ('id', 'username', 'email', 'password1', 'password2')
        extra_kwargs = {'password':{'write_only':True}}

        def validate(self, attrs):
            if attrs['password1'] != attrs['password2']:
                raise serializers.ValidationError("Passwords do not match")
            
            password = attrs.get('password1', '')
            if len(password) < 8:
                raise serializers.ValidationError('Password must be at least 8 characters!')

        def create(self, validated_data):
        # Extract password data from validated data
            password = validated_data.pop('password1')
            validated_data.pop('password2')
        
        # Create employee instance
            return Employees.objects.create_user(password=password, **validated_data)


class EmployeeLoginSerializer(serializers.Serializer):
    """Login Serializer for Employees"""
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorect Login Credentials')

