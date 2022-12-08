from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudenstSerializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def Student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id', None)


        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudenstSerializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = Student.objects.all()
        serializerw = StudenstSerializers(stu, many=True)
        json_data = JSONRenderer().render(serializerw.data)
        return HttpResponse(json_data, content_type='application/json')
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        pythonData = JSONParser().parse(stream)
        serializer = StudenstSerializers(data=pythonData)

        if serializer.is_valid():
            serializer.save()

            res = {'msg':'Data successfully saved!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudenstSerializers(stu, data=pythonData)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data successfully Updated!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        data = request.body
        stream = io.BytesIO(data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'successfully deleted!'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')

        return JsonResponse(res, safe=False)
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')
        


        
