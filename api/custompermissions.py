from rest_framework.permissions import BasePermission

class Mypermissions(BasePermission):
    def has_permission(self,request,view):
        if request.method=="POST":
        # if request.method=="POST" or request.method=="GET":
            return True
        else:
            return False
