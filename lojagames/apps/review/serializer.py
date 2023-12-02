from .models import Review
from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    review = serializers.CharField() 
    rating = serializers.IntegerField()
    release_date = serializers.DateField()
    
    def create(self, data):
        return Review.objects.create(**data)


    class Meta:
        model = Review
        fields = '__all__'