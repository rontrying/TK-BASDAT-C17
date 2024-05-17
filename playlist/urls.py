from django.urls import path
from .views import *

urlpatterns = [
    path('', user_playlist, name='user_playlist'),
    path('tambah-playlist/', tambah_playlist, name='tambah_playlist'),
    path('playlist-details/<uuid:id_user_playlist>/', playlist_details, name='playlist_details'),
    path('playlist-details/<uuid:id_user_playlist>/tambah-lagu/', tambah_lagu, name='tambah_lagu'),
    path('update-playlist/<uuid:id_user_playlist>/', update_playlist, name='update_playlist'),
    path('delete-playlist/<uuid:id_user_playlist>/', delete_playlist, name='delete_playlist'),
]