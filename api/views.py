from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets

# Create your views here.
class StudetModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    