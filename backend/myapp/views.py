from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from myapp.models import *
from myapp.serializers import *
from myapp.permissions import *
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from django.conf import settings
import uuid


# Create your views here.
class GenerateTemporaryTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")

        if not email:
            return Response({'detail': 'Email is required.'}, status= status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'detail': 'Email is already registered.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            # Create a temporary token
            token = TemporaryToken.objects.create(
                email=email,
                expires_at=timezone.now()+ timedelta(hours=1)
            )
            send_mail(
                'Your Signup Token',
                f'Use this token to signup: {token.token}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return Response({'message': 'Token sent to email.'}, status= status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class ValidateTokenView(APIView):
    """Validates Token"""
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        token = request.data.get("token")
        if not email or not token:
            return Response({'detail': 'Token and email are required.'}, status= status.HTTP_400_BAD_REQUEST)
        try:
            temp_token = TemporaryToken.objects.get(token=token, email=email) # query token from database
            if temp_token.is_valid():
                return Response({'valid': True}, status= status.HTTP_200_OK)
            else:
                return Response({'valid': False, 'message': 'Token expired.'}, status= status.HTTP_400_BAD_REQUEST)
        except TemporaryToken.DoesNotExist:
            return Response({'valid': False, 'message': 'Invalid token.'}, status= status.HTTP_404_NOT_FOUND)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class EmployeeRegistrationAPIView(GenericAPIView):
    """Employee Registration Api"""
    permission_classes = (AllowAny,)
    serializer_class = EmployeeRegistrationSerializer

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        email = request.data.get('email')
        if not token or not email:
            return Response({'detail': 'Email and Token required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            temp_token = TemporaryToken.objects.get(token=token, email=email)

            if not temp_token.is_valid():
                return Response({'detail': 'Token has expired.'}, status= status.HTTP_400_BAD_REQUEST)
            
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            # Generate JWT tokens for the new user
            refresh_token = RefreshToken.for_user(user)
            data = serializer.data
            data['tokens'] = {"refresh":str(refresh_token),
                          "access": str(refresh_token.access_token)}
            temp_token.delete()
            
            return Response(data, status= status.HTTP_201_CREATED)
        
        except TemporaryToken.DoesNotExist:
            return Response({'detail': 'Invalid Token.'}, status= status.HTTP_404_NOT_FOUND)
    

class EmployeeLoginAPIView(GenericAPIView):
    """Employee Login Api"""
    permission_classes = (AllowAny,)
    serializer_class = EmployeeLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = EmployeeSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['tokens'] = {"refresh":str(token),
                          "access": str(token.access_token)}
        return Response(data, status= status.HTTP_201_CREATED)
        
        
class EmployeeLogoutAPIView(GenericAPIView):
    """Logout Api for employee"""
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status= status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        

class PatientList(ListCreateAPIView):
    """API to view patient list and create new patient"""
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [AllowAny]


class PatientDetails(RetrieveUpdateDestroyAPIView):
    """To update a patient's record"""
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [AllowAny]


class MedicationList(ListCreateAPIView):
    """API to view medication"""
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [AllowAny]


class MedicationDetails(RetrieveUpdateDestroyAPIView):
    """To update medications"""
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [AllowAny]


class PrescriptionList(ListCreateAPIView):
    """API to view patient prescriptions"""
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [AllowAny]


class PrescriptionDetails(RetrieveUpdateDestroyAPIView):
    """To update a patient's prescription"""
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [AllowAny]


class PrescriptionMedList(ListCreateAPIView):
    """API for linking prescription and medication"""
    queryset = PrescriptionMedication.objects.all()
    serializer_class = PrescriptionMedicationSerializer
    permission_classes = [AllowAny]


class PrescriptionMedDetails(RetrieveUpdateDestroyAPIView):
    """To update medication quantity when order is fulfilled"""
    queryset = PrescriptionMedication.objects.all()
    serializer_class = PrescriptionMedicationSerializer
    permission_classes = [AllowAny]


class OrderList(ListCreateAPIView):
    """API for prescription order"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]


class OrderDetails(RetrieveUpdateDestroyAPIView):
    """To update prescription orders"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]


class AppointmentList(ListCreateAPIView):
    """API for appointments"""
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]


class AppointmentDetails(RetrieveUpdateDestroyAPIView):
    """To update appointments"""
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]

    