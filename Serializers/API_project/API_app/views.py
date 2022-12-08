from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerilizer
from django.http import HttpResponse
# Create your views here.

def Student_view(request, pk):
    student = Student.objects.get(id=pk)
    serializers = StudentSerilizer(student)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data, content_type='application/json')


def Student_list(request):
    student = Student.objects.all()
    serializer = StudentSerilizer(student, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
