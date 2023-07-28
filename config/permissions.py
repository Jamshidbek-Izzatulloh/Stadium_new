from rest_framework.permissions import BasePermission


class OwnerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 'o':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user