from django.urls import path, include
from myapp.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'signup', SignupViewSet, basename='signup')
router.register(r'departments', DepartmentsViewSet)
router.register(r'patients', PatientViewSet)
# router.register(r'patientfolders', PatientFolderViewSet)
# router.register(r'patientprofiles', UserProfileViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('employees/signup/', EmployeesSignupView.as_view(), name='employees-signup'),
    path(r'', include(router.urls)),
]
