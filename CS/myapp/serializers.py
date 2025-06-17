from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from myapp.models import *
from rest_framework import serializers


Employee = get_user_model()
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
        fields = '__all__'
        extra_kwargs = {'password':{'write_only':True}}

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match")
            
        password = attrs.get('password1', '')
        if len(password) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters!')
        validate_password(password)
        return attrs

    def create(self, validated_data):
    # Extract password data from validated data
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        
        # Create user instance
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password  # Set password securely using create_user
        )
        user.is_staff = True
        user.is_active = False
        user.save()

        # Create the Employee profile
        employee = Employees.objects.create(
            user=user,
            **validated_data
        )

        return employee


class EmployeeLoginSerializer(serializers.Serializer):
    """Login Serializer for Employees"""
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        # Ensure email and password are provided
        if not email or not password:
            raise serializers.ValidationError({"non_field_errors": ["Email and password are required."]})

        # Check if the Employee exists
        try:
            employee = Employees.objects.select_related("user").get(email=email)
        except Employees.DoesNotExist:
            raise serializers.ValidationError({"non_field_errors": ["Incorrect Login Credentials"]})

        user = getattr(employee, 'user', None)  # Get the related User instance

        # Ensure user exists and check password
        if user is None or not user.check_password(password):
            raise serializers.ValidationError({"non_field_errors": ["Incorrect Login Credentials"]})

        # Ensure user is active
        if not user.is_active:
            raise serializers.ValidationError({"non_field_errors": ["User account is inactive."]})

        return user 


class PatientSerializer(serializers.ModelSerializer):
    """Patient Serializer"""
    class Meta:
        model = Patient
        fields = '__all__'

       
class MedicationSerializer(serializers.ModelSerializer):
    """Medication Serializer"""
    class Meta:
        model = Medication
        fields = '__all__'


class PrescriptionSerializer(serializers.ModelSerializer):
    """Prescription Serializer"""
    class Meta:
        model = Prescription
        fields = '__all__'


class PrescriptionMedicationSerializer(serializers.ModelSerializer):
    """Prescription Serializer"""
    class Meta:
        model = PrescriptionMedication
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """Prescription Order Serializer"""
    class Meta:
        model = Order
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    """Appointment Serializer"""
    class Meta:
        model = Appointment
        fields = '__all__'