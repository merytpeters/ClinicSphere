from django.urls import path, include
from patientportal.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'patientprofile', UserProfileViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]