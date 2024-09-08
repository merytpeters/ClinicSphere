from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from myapp.models import *
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentName')


class UserSerializer(serializers.ModelSerializer):
    """Serializer for creating a User along with an Employee"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer for creating an employee, including User creation"""
    user = UserSerializer()

    class Meta:
        model = Employees
        fields = ('user',
                  'EmployeeName',
                  'Department',
                  'DateEmployed',
                  'Employees_Title')

    def create(self, validated_data):
        # Extract user data from validated data
        user_data = validated_data.pop('user')
        # Create user instance
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )
        # Create employee instance
        employee = Employees.objects.create(user, **validated_data)
        return employee


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Signup
        fields = ['email', 'username', 'password', 'created_at']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Signup(**validated_data)
        user.password = make_password(password)
        user.save()
        return user


# class LoginSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
# class Meta:

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['first_name',
                  'last_name',
                  'date_of_birth',
                  'gender',
                  'address',
                  'phone_number',
                  'email',
                  'medical_record_number',
                  'date_registered',
                  'weight',
                  'height',
                  'blood_type',
                  'genotype']

        def validate(self, data):
            if data.get('weight') and data['weight'] <= 0:
                raise serializers.ValidationError(
                    {"Weight must be a positive number"}
                    )
            if data.get('height') and data['height'] <= 0:
                raise serializers.ValidationError(
                    {"Height must be a positive number"}
                    )
            return data

