from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class StudentApi(APIView):

    def get(self,request,pk=None,formate=None): 
        if pk is not None:
            stu=Student.objects.get(pk=pk)
            serializer=StudentSerializer(stu)
            return Response(serializer.data,status=status.HTTP_302_FOUND)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_302_FOUND)

    def post(self,request,pk=None,formate=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Account Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors(),status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,pk=None,formate=None):
        stu=Student.objects.get(pk=pk)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'},status=status.HTTP_426_UPGRADE_REQUIRED)
        return Response(serializer.errors(),status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,pk=None,formate=None):
        stu=Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg':'Data Deleted'},status=status.HTTP_200_OK)