from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField() 
    address = serializers.CharField()   
    cell_phone = serializers.CharField()
    email = serializers.EmailField()
    gender = serializers.CharField()
    birth_date = serializers.DateField()

    def create(self, data):
        return User.objects.creat(**data)
