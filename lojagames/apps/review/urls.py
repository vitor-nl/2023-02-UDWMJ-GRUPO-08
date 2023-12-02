from django.urls import path, include
from .views import review_list, review_create

app_name = 'review'
urlpatterns = [
    path('', review_create),
    path('list/', review_list)
]