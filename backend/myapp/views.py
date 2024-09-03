from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# from django.views.decorators.csrf import csrf_exempt
from myapp.models import *
from myapp.serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class HomePageView(View):
    def get(self, request):
        return HttpResponse("Welcome to homepage")


class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


class SignupViewSet(viewsets.ModelViewSet):
    serializer_class = SignupSerializer
    queryset = Signup.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LoginView(APIView):
    def post(self, request):
        identifier = request.data.get('username_or_email')
        password = request.data.get('password')

        try:
            user_obj = User.objects.get(email=identifier)
            username = user_obj.username
        except User.DoesNotExist:
            username = identifier

        user = authenticate(request, username=identifier, password=password)
        if user is not None:
            login(request, user)
            return Response(
                {"message": "Login successful"},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Invalid Credentials"},
                status=status.HTTP_400_BAD_REQUEST
            )


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class PatientFolderViewSet(viewsets.ModelViewSet):
    seralizer_class = PatientFolderSerializer
    queryset = PatientFolder.objects.all()
