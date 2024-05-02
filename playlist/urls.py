from django.urls import path
from .views import *

urlpatterns = [
    path('', user_playlist, name='user_playlist'),
    path('tambah-playlist/', tambah_playlist, name='tambah_playlist'),
    path('playlist-details/', playlist_details, name='playlist_details'),
]