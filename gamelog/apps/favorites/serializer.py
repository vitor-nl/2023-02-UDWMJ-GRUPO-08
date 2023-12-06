from .models import Favorites
from rest_framework import serializers

class FavoritesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    review_name = serializers.CharField()
    description = serializers.CharField()
    release_date = serializers.DateField()
    
    def create(self, data):
        return Favorites.objects.create(**data)
    

    def update(self, instance, data):
        instance.created_by = data.get('created_by', instance.created_by)
        instance.review_name = data.get('review_name', instance.review_name)
        instance.description = data.get('description', instance.description)
        instance.release_date = data.get('release_date', instance.release_date)

        instance.save()
        return instance


    class Meta:
        model = Favorites
        fields = '__all__'