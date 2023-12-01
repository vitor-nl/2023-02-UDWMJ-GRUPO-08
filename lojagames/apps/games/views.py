from django.shortcuts import render
from django.http import JsonResponse
#from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from games.models import Games
from games.serializer import GamesSerializer

# Create your views here.

@api_view(['GET'])
def game_list(request):
    games = Games.objects.all()
    serializer = GamesSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def game_create(request):
    serializer = GamesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors) 



#class GamesViewSet(viewsets.ModelViewSet):
#  queryset = Games.objects.all()
#  serializer_class = GamesSerializer