from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Favorites
from review.models import Review
from rest_framework.permissions import IsAuthenticated
from .serializer import FavoritesSerializer

# Create your views here.

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_favorties(request):
    favorites = Favorites.objects.all()
    serializer = FavoritesSerializer(favorites, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def favorites_add(request):
    if 'review_name' not in request.data:
        return Response({'error': 'O campo review_name é obrigatório'})
    
    review_name = request.data['review_name']
    
    try:
        review = Review.objects.get(name=review_name)
    except Review.DoesNotExist:
         return Response({'error': f'A Review com o nome {review_name} não foi encontrada.'}, status=status.HTTP_404_NOT_FOUND)
    
    favorites_data = {
        'review_name': review.name,
        'description': review.description,
        'release_date': review.release_date,  # Corrigido o typo aqui
    }
    favorites_data.update(request.data)

    serializer = FavoritesSerializer(data=favorites_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def favorites(request, pk):
    try:
        favorites = Favorites.objects.get(pk=pk)
    except:
        return Response({
            'error': 'This item does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FavoritesSerializer(favorites)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = FavoritesSerializer(favorites, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return serializer.errors
    
    if request.method == 'DELETE':
        favorites.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)