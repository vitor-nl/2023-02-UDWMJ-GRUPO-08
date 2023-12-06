﻿from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from .serializer import UserSerializer
from .models import User
from django.contrib.auth import login, logout

#Create your views here.

def menu(request):
    return render(request,'menu.html')


@permission_classes([AllowAny,])
def user_register(request):
    render(request,'register.html', {'user_register':user_register})
    if request.method == 'POST':
        serializer = UserSerializer(data = request.POST)
        if serializer.is_valid():
            serializer.save()
            return render(request,'menu.html')
    return render(request,'register.html', {'user_register':user_register})


@permission_classes([AllowAny])
def user_login(request):
    render(request,'login.html', {'user_login':user_login})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = None
        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            login(request, user)
            
        return render(request,'login.html', {'user_login':user_login})

        
    return render(request,'login.html', {'user_login':user_login})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            logout(request)
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


'''
@api_view(['POST'])
def user_register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data['response']=  "New user created successfully"
            data['username'] = user.username
            data['email'] = user.email
        else:
            data = serializer.errors
        return Response(data)
'''