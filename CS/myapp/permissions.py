from myapp.models import Employees
from rest_framework.permissions import BasePermission


class IsEmployee(BasePermission):
    """Custom permission to allow only Employees to sign up"""
    def has_permission(self, request, view):
        # if view.action == 'create':
        return request.user and request.user.is_authenticated and\
            request.user.groups.filter(name='Employees').exists()
