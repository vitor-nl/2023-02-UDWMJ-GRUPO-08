from django.urls import path
from user.views import user_create, user_list, user

app_name = 'user'
urlpatterns = [
    path('', user_create),
    path('list/', user_list),
    path('<int:pk>', user),
]
