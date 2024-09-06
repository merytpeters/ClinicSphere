from myapp.models import Employees
from rest_framework.permissions import BasePermission


class IsEmployee(BasePermission):
    """Custom permission to allow only Employees to sign up"""
    def has_permission(self, request, view):
        # if view.action == 'create':
        return request.user and request.user.is_authenticated and\
            request.user.groups.filter(name='Employees').exists()


class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and\
            hasattr(request.user, 'userprofile') and\
            request.user.userprofile.is_patient
