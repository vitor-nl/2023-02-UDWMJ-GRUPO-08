from django.urls import path, include
from .views import view_wishlist, wishlist_add, wishlist

app_name = 'wishlist'
urlpatterns = [
    path('', wishlist_add),
    path('viewwishlist/', view_wishlist),
    path('<int:pk>', wishlist)
]