from .models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from user.serializer import UserSerializer

# Create your views here.
@api_view(['GET'])
def user_list(request):
    users = User.objects.all() #Complex Data
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
def user_create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    

@api_view(['GET', 'PUT', 'DELETE'])
def user(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return serializer.errors
    
    if request.method == 'DELETE':
        user.delete()
        return Response({
            'delete': True
        })
    