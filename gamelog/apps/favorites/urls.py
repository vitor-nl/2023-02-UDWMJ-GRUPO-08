from django.urls import path
from .views import view_favorties, favorites_add, favorites

app_name = 'favorites'
urlpatterns = [
    path('', favorites_add),
    path('list/', view_favorties),
    path('<int:pk>', favorites)
]