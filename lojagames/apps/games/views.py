from django.shortcuts import render
from django.http import JsonResponse
from games.models import Games
from rest_framework import viewsets
from games.serializer import GamesSerializer

# Create your views here.

def game_list(request):
    games = Games.objects.all()
    gamesPython = list(games.values())
    return JsonResponse({
        'games' : gamesPython
    })

#class GamesViewSet(viewsets.ModelViewSet):
#  queryset = Games.objects.all()
#  serializer_class = GamesSerializer 