from rest_framework.permissions import BasePermission

class isBlogAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'is_blog_admin', False )
    


class isQA(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'is_qa', False )