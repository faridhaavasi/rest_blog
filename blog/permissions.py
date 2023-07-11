from rest_framework import permissions
from .models import Post
class AlowUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        username_post = Post.objects.filter(user__username=request.user.username).exists()
        return username_post
