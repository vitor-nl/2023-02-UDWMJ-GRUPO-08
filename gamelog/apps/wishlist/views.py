from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Wishlist
from rest_framework.permissions import IsAuthenticated
from .serializer import WishlistSerializer

# Create your views here.

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_wishlist(request):
    wishlist = Wishlist.objects.all()
    serializer = WishlistSerializer(wishlist, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def wishlist_add(request):
    serializer = WishlistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def wishlist(request, pk):
    try:
        wishlist = Wishlist.objects.get(pk=pk)
    except:
        return Response({
            'error': 'This item does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = WishlistSerializer(wishlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return serializer.errors
    
    if request.method == 'DELETE':
        wishlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)