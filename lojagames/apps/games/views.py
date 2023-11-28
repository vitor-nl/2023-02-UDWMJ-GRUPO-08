from django.shortcuts import render

from .models import Games
from rest_framework import viewsets
from .serializer import GamesSerializer

# Create your views here.

class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer 