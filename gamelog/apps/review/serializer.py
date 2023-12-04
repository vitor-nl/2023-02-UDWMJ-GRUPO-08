from .models import Review
from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    review = serializers.CharField() 
    rating = serializers.FloatField()
    release_date = serializers.DateField()
    
    def create(self, data):
        return Review.objects.create(**data)
    

    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.description = data.get('description', instance.description)
        instance.review = data.get('review', instance.review)
        instance.rating = data.get('rating', instance.rating)
        instance.release_date = data.get('release_date', instance.release_date)

        instance.save()
        return instance


    class Meta:
        model = Review
        fields = '__all__'