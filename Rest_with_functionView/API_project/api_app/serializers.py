from rest_framework import serializers

from .models import Studet

class Student_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=250)