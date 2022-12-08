from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'massage':'Data successfully added!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(res.data)
        return HttpResponse(json_data, content_type='application/json')