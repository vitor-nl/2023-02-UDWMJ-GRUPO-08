from django.urls import path
from .views import base,user_register,user_login, user_logout


app_name = 'user'
urlpatterns = [
    path('',base, name='base'),
    path('register/',user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]

