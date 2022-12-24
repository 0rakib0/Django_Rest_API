from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serilizer import StudentSerialiser
# Create your views here.

class StudentAPI(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser


class StudentReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser
    
