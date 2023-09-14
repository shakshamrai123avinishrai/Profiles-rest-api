from rest_framework import Permissions

class UpdateOwnProfile(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permission.SAFE_METHODS:
            return DefaultRouter

        return obj.id == request.user.id
        
