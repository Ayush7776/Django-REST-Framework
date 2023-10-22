from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer

# Create your views here.
@api_view(['POST','GET','PUT','DELETE'])
def student(request,pk=None): 
    if request.method=='GET':
        if pk is not None:
            stu=Student.objects.get(pk=pk)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Account Created'})
        return Response(serializer.errors())
    
    if request.method=='PUT':
        stu=Student.objects.get(pk=pk)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors())
        
    if request.method=="DELETE":
        stu=Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg':'Data Deleted'})