from rest_framework import serializers

from .models import Student

# -------------------------------> validators <----------------------------------------

def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("Name Shuld start with 'R' ")


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100, validators=[start_with_r])


    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    

    # --------------------------> Field Level validation <--------------------------------

    # (def validate_roll(self, value):
    #     if value >=200:
    #         raise serializers.ValidationError('Please Enter under 200 roll!')
    #     elif value <100:
    #         raise serializers.ValidationError('Please Enter 100 + roll!')
    #     return value)

    # --------------------------> Objects Level validation <--------------------------------    

    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')

    #     if nm.lower() == 'foysal' and ct.lower() != 'dhaka':
    #         raise serializers.ValidationError('City Must be Dhaka!')
    #     return data
        