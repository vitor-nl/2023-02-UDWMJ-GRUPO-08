from django.contrib import admin
from django.urls import path, include
from games.views import game_list

app_name = 'games'
urlpatterns = [
    path('list/', game_list)
]