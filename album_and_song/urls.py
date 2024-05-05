from django.urls import path
from .views import *
app_name = 'album_and_song'

urlpatterns = [
    path('', create_album, name='create_album'),
    path('create_lagu/', create_lagu, name="create_lagu"),
    path('list_album/',list_album,name='list_album'),
    path('daftar_lagu/<str:nama_album>/',daftar_lagu,name='daftar_lagu')
]