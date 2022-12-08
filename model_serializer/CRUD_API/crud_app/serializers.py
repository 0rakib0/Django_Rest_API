from rest_framework import serializers

from .models import Student

def rakib(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Need to start with r')

    return value


class StudenstSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=500 , validators=[rakib])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['name', 'city']
        # extra_kwargs = {'name':{'read_only':True}}



    # def validate_roll(self, value):
    #     if value >100:
    #         raise serializers.ValidationError('Need to inpute Less 100')
    #     return value
    


# class StudenstSerializers(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

#     def create(self, validate_data):
#         return Student.objects.create(**validate_data)


    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.roll = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()
#         return instance