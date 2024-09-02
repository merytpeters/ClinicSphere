from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# from django.views.decorators.csrf import csrf_exempt
from myapp.models import Signup
from myapp.serializers import SignupSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class HomePageView(View):
    def get(self, request):
        return HttpResponse("Welcome to homepage")

class SignupViewSet(viewsets.ModelViewSet):
    serializer_class = SignupSerializer
    queryset = Signup.objects.all()


class LoginView(APIView):
    def post(self, request):
        identifier = request.data.get('username_or_email')
        password = request.data.get('password')
        user = authenticate(request, username=identifier, password=password)
        if user is not None:
            login(request, user)
            return Response({"Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"Error: Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
