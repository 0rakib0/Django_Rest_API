from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['POST', 'GET'])
def StudentApi(request):
        if request.method == 'POST':
            print(request.data)
            return Response({'msg':'Hello Bnagladesh I am POST request', 'data':request.data})
        elif request.method == 'GET':
            print('Hey! I am From Get Request!')
            return Response({'Hello':'Hello Bangladesh I am from Get Request'})