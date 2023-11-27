from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField() 
    address = serializers.CharField()   
    cell_phone = serializers.CharField()
    email = serializers.EmailField()
    gender = serializers.CharField()
    birth_date = serializers.DateField()
    password = serializers.CharField()

    def create(self, data):
        return User.objects.create(**data)
    
    def update(self, instance, data):
        instance.first_name = data.get('Nome',instance.first_name)
        instance.last_name = data.get('Sobrenome',instance.last_name)
        instance.address = data.get('Endereco',instance.address)
        instance.cell_phone = data.get('Telefone celular',instance.cell_phone)
        instance.email = data.get('E-mail',instance.email)
        instance.gender = data.get('Genero',instance.gender)
        instance.birth_date = data.get('Data de nascimento',instance.birth_date)
        instance.password = data.get('Senha',instance.password)
        
        instance.save()
        return instance
