from django.urls import path
from myapp.views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('registration/', EmployeeRegistrationAPIView.as_view(), name='register-employee'),
    path('login/', EmployeeLoginAPIView.as_view(), name='logout-user'),
    path('logout/', EmployeeLogoutAPIView.as_view(), name='logout-user'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token'),
]
