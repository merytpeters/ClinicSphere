from django.shortcuts import render
from django.contrib.auth import authenticate, login
from patientportal.models import *
from patientportal.serializers import *
#from patientportal.permissions import *
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
