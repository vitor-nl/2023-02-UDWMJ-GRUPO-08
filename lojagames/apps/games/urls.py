from django.urls import path, include
from games.views import game_list, game_create

app_name = 'games'
urlpatterns = [
    path('', game_create),
    path('list/', game_list)
]