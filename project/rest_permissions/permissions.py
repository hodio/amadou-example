from rest_framework import permissions


class Octal(permissions.BasePermission):

    def has_permission(self, request, view):
        # TODO 
        # We need to introspect the model to get the perms_octal_default
        
        return True

    def has_object_permission(self, request, view, obj):
        
        perms = obj.perms_octal
        
        # set perm index for guest
        perm_index = 2
        
        # set perm index for group
        for request.user.groups.all() as group:
            if obj.group == group:
                perm_index = 1

                     
        # set perm index for owner
        if request.user == obj.owner:
            perm_index = 0
            
        # evaluate
   
        # read - only = 4
        if requet.method == "GET":
            if perms[perm_index] >= 4 :
                return True
            else:
                return False

        # write - only = 2, &read = 6
        elif request.method == "POST":
            if perms[perm_index] == 2 || perms[perm_index] == 3 || perms[perm_index] >= 6 :
                return True
            else:
                return False
  
        # edit and delete  - only = 1, &read = 5, &write = 3, &read&write = 7     
        elif request.method == "PUT" || request.method == "DELETE":
            if perms[perm_index] == 1 || perms[perm_index] == 3 || perms[perm_index] == 5 || perms[perm_index] == 7 :
                return True
            else:
                return False

class CustomObjectPermissions(permissions.DjangoObjectPermissions):
    """
    Similar to `DjangoObjectPermissions`, but adding 'view' permissions.
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }  