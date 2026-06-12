from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsClubAdmin(BasePermission):
    """
    Allows access only to users with the 'ADMIN' role in MongoDB.
    """
    def has_permission(self, request, view):
        
        if not request.user or not isinstance(request.user, dict):
            return False
            
        return request.user.get('role') == 'ADMIN'


class IsTeamLeadOrAdmin(BasePermission):
    """
    Allows access to both Admins and Team Leads.
    """
    def has_permission(self, request, view):
        if not request.user or not isinstance(request.user, dict):
            return False
            
        return request.user.get('role') in ['ADMIN', 'TEAM_LEAD']