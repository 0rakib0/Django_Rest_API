from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from .models import Student
from .serilizers import StudentSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def Create_Student(request):
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        pythoData = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythoData)

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data successfully save!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')