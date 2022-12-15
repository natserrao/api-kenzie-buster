from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, user: User) -> bool:
        if request.user.is_employee:
            return True

        if user.id == request.user.id and request.user.is_employee == False:
            return True
