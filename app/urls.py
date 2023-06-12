from django.urls import path
from .views import *

urlpatterns = [
    path('', posts, name="home"),
    path('user/<str:username>/posts/', users_posts, name='users_posts'),
    path('user/me/', user_posts, name='user_posts')
]