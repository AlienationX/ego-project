from rest_framework.permissions import BasePermission
from server.settings import SECRET_KEY


class HasAccessKey(BasePermission):
    def has_permission(self, request, view):
        access_key = request.headers.get('Access-Key', None)
        valid_access_key = "django-insecure-88hefbg6c!mrv5x(xa4swy-h3y41f()(8xh6syj(xi&m!!h$#b"  # 替换为你的密钥
        return access_key == valid_access_key
        # return access_key == SECRET_KEY


class IsSuperUser(BasePermission):
    """
    仅允许超级管理员访问
    """
    message = "仅超级管理员可访问此接口"

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
