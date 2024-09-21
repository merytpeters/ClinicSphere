from django.urls import path
from myapp.views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('generate-token/', GenerateTemporaryTokenView.as_view(), name='generate-token'),
    path('validate-token/<uuid:token>/', ValidateTokenView.as_view(), name='validate-token'),
    path('registration/', EmployeeRegistrationAPIView.as_view(), name='register-employee'),
    path('login/', EmployeeLoginAPIView.as_view(), name='logout-user'),
    path('logout/', EmployeeLogoutAPIView.as_view(), name='logout-user'),
    path('patients/', PatientList.as_view(), name='patients-files'),
    path('patientfile/<int:pk>/', PatientDetails.as_view(), name='patient'),
    path('medications/', MedicationList.as_view(), name='medications'),
    path('update-medications/<int:pk>/', MedicationDetails.as_view(), name='update-medications'),
    path('prescriptions/', PrescriptionList.as_view(), name='prescriptions'),
    path('update-prescription/<int:pk>/', PrescriptionDetails.as_view(), name='update-prescription'),
    path('medication-quantity/', PrescriptionMedList.as_view(), name='medication-quantity'),
    path('update-medication-quantity/<int:pk>/', PrescriptionMedDetails.as_view(), name='update-medication-quantity'),
    path('orders/', OrderList.as_view(), name='order'),
    path('update-orders/<int:pk>/', OrderDetails.as_view(), name='update-orders'),
    path('appointments/', AppointmentList.as_view(), name='appointment'),
    path('update-appointment/<int:pk>/', AppointmentDetails.as_view(), name='update-appointment'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token'),
]
