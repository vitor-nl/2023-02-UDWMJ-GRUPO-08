from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'games'

router = routers.DefaultRouter()
router.register('games', views.ProductViewSet, basename='games')

urlpatterns = [
    path('', include(router.urls) )
]