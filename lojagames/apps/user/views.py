from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import UserSerializer
from .models import User
from django.shortcuts import render,redirect

#Create your views here.

def home(request):
    return render(request,'home.html')

@api_view(['POST'])
def user_register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            User = serializer.create()
            data['response']=  "New user crated successfully"
            data['username'] = User.username
            data['email'] = User.email
        else:
            data = serializer.errors
        return Response(data)