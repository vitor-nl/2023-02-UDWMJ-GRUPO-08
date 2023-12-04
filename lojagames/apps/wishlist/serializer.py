from .models import Wishlist
from rest_framework import serializers
from .models import Wishlist

class WishlistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    release_date = serializers.DateField()
    
    def create(self, data):
        return Wishlist.objects.create(**data)
    

    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.description = data.get('description', instance.description)
        instance.price = data.get('price', instance.price)
        instance.release_date = data.get('release_date', instance.release_date)

        instance.save()
        return instance


    class Meta:
        model = Wishlist
        fields = '__all__'