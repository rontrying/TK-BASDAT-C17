from django.urls import path
from .views import *

urlpatterns = [
    path('', user_playlist, name='user_playlist'),
]