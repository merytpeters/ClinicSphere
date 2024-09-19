from django.urls import path
from patientportal.views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('setpassword/', PasswordSetView.as_view(), name='setpassword'),
    path('patientlogin/', UserLoginAPIView.as_view(), name='login'),
    path('patientlogout/', UserLogoutAPIView.as_view(), name='logout'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token'),
]