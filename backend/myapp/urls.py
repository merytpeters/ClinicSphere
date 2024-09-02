from django.urls import path, include
from myapp.views import SignupViewSet, HomePageView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'signups', SignupViewSet)

urlpatterns = [
    path('', HomePageView.as_view(), name='Homepage'),
    path('api/login/', LoginView.as_view(), name='login'),
    path(r'', include(router.urls)),
]
