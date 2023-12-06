from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Favorites
from rest_framework.permissions import IsAuthenticated
from .serializer import FavoritesSerializer

# Create your views here.

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_favorties(request):
    Favorites = Favorites.objects.all()
    serializer = FavoritesSerializer(favorites, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def favorites_add(request):
    serializer = FavoritesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def favorites(request, pk):
    try:
        Favorites = Favorites.objects.get(pk=pk)
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