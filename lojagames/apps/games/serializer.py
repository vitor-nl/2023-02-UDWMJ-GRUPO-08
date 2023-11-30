from games.models import Games
from rest_framework import serializers
from games.models import Games

class GamesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    review = serializers.CharField() 
    note = serializers.IntegerField()
    release_date = serializers.DateField()
    
    def create(self, data):
        return Games.objects.create(**data)


    #class Meta:
    #    model = Games
    #    fields = '__all__'