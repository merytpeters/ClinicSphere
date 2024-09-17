from django.contrib.auth import authenticate
from myapp.models import *
from myapp.serializers import *
from myapp.permissions import *
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView


# Create your views here.
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

"""class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class EmployeesSignupView(generics.CreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class SignupViewSet(viewsets.ModelViewSet):
    serializer_class = SignupSerializer
    queryset = Signup.objects.all()
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsEmployee()]
        return [IsAuthenticated()]


class LoginView(APIView):
    def post(self, request):
        identifier = request.data.get('username_or_email')
        password = request.data.get('password')

        # try to get user by email, or username if email not found
        user = None
        if identifier:
            try:
                user = User.objects.get(email=identifier)
            except User.DoesNotExist:
                user = user.objects.filter(username=identifier).first()

        if user is not None and authenticate(
            request, username=user.username, password=password
        ):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                "message": "Login successful"
                }, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid Credentials"},
                status=status.HTTP_400_BAD_REQUEST
            )



class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]"""

