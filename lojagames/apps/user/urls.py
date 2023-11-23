from django.urls import path, include
from user.views import user_create, users
from rest_framework import routers

app_name = 'user'
urlpatterns = [
    path('', user_create),
    path('list/', users)
]
