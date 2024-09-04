from django.urls import path, include
from myapp.views import SignupViewSet, HomePageView, LoginView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'signup', SignupViewSet, basename='signup')

urlpatterns = [
    path('', HomePageView.as_view(), name='Homepage'),
    path('login/', LoginView.as_view(), name='login'),
    path(r'', include(router.urls)),
]
