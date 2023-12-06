from .models import Favorites
from rest_framework import serializers

class FavoritesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    release_date = serializers.DateField()
    
    def create(self, data):
        return Favorites.objects.create(**data)
    

    def update(self, instance, data):
        instance.created_by = data.get('created_by', instance.created_by)
        instance.name = data.get('name', instance.name)
        instance.description = data.get('description', instance.description)
        instance.release_date = data.get('release_date', instance.release_date)

        instance.save()
        return instance


    class Meta:
        model = Favorites
        fields = '__all__'