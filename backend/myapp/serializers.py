from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from myapp.models import Departments, Employees, Patient, Signup, PatientFolder
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fileds = ('DepartmentName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeName',
                  'Department',
                  'DateEmployed')


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


class UserSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'patient']

    def create(self, validated_data):
        patient_data = validated_data.pop('patient')
        user = User.objects.create_user(**validated_data)
        Patient.objects.create(user=user, **patient_data)
        return user


class PatientFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientFolder
        fields ='__all__'
