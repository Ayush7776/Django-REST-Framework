from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrive(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


