from django.urls import path
from .views import *

app_name = 'song'

urlpatterns = [
    path('details/<uuid:id_konten>/', song_details, name='song_details'),
    path('tambah-lagu/<uuid:id_konten>/', tambah_lagu_ke_playlist, name='tambah_lagu_ke_playlist'),
    path('add-song-to-playlist/<uuid:id_konten>/', add_song_to_playlist, name='add_song_to_playlist'),
    path('download/<uuid:id_konten>/', download_song, name='download_song'),
    path('play/<uuid:id_konten>/', play_song, name='play_song'),
]
