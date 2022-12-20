from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class studen_api(APIView):
    def get(self, request, forma=None, id=None):
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    def post(self,request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def put(self,request, id=None,format=None):
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'All data updated successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def patch(self,request, id=None,format=None):
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Single data updated successfully'})
        return Response(serializer.errors)



    def delete(self,request, id=None,format=None):
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Successfully Deleted!'})

# @api_view(['GET', 'POST', 'PATCH', 'PUT','DELETE'])
# def studen_api(request, id=None):
#     if request.method == 'GET':
#         # id = request.data.get('id')

#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)

#     if request.method == 'PUT':
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'All data updated successfully'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
    
#     if request.method == 'PATCH':
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Single data updated successfully'})
#         return Response(serializer.errors)
    
#     if request.method == 'DELETE':
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         return Response({'msg':'Data Successfully Deleted!'})

