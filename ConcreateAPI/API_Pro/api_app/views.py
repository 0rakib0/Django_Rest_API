from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serilizer import StudentSerialiser
# Create your views here.

class cr(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser


class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser

class StudentAdd(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser

class StudentRet(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser

class StudentUp(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser

class StudentDe(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser



class RU(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser

class RD(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser


class rud(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser