from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class StudetModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    # We Can Creat Auth-Token Using Following Command 
    # python manage.py drf_create_token (username) 


    # authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
