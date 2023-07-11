from rest_framework import permissions
from .models import Blacked
class BlocklistPermission(permissions.BasePermission):


    def has_permission(self, request, view):
        username = request.user.username
        blocked = Blacked.objects.filter(username=username).exists()
        return not blocked

