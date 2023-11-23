from django.shortcuts import render
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from user.serializer import UserSerializer

# Create your views here.
@api_view(['GET'])
def users(request):
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