from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student
from .serilizer import StudentSerialiser
# Create your views here.

class StudentAPI(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serilizer = StudentSerialiser(stu, many=True)
        return Response(serilizer.data)
    
    def retrieve(self, request, pk=None):
        stu = Student.objects.get(id=pk)
        serializer = StudentSerialiser(stu)
        return Response(serializer.data)
    
    def create(self, request):
        serilizer = StudentSerialiser(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data susseccfully saved!'})
        return Response(serilizer.errors)
    
    def update(self, request, pk=None):
        stu = Student.objects.get(id=pk)
        serializer = StudentSerialiser(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Update Susseccfully!'})
        return Response(serializer.errors)
    
    def partial_update(self, request, pk=None):
        stu = Student.objects.get(id=pk)
        serializer = StudentSerialiser(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Update Susseccfully!'})
        return Response(serializer.errors)
    
    def destroy(self, request, pk=None):
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg':'Student Successfully deleted!'})
