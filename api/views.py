from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

# Create your views here.
class StudetModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    authentication_classes=[BasicAuthentication]
    # This Will Be Only Take Permission To Staff Status True In Admin Panel
    permission_classes=[IsAdminUser]


    