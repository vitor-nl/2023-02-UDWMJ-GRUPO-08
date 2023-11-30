from games.models import Games
from rest_framework import serializers

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = '__all__'