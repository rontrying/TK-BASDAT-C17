from django.urls import path
from album_and_song.views import *
app_name = 'album_and_song'

urlpatterns = [
    path('', create_album, name='create_album'),
    path('create_lagu/<str:id_album>/', create_lagu, name="create_lagu"),
    path('list_album/',list_album,name='list_album'),
    path('daftar_lagu/<str:id_album>/',daftar_lagu, name='daftar_lagu'),
    path('delete_album/<str:id_album>/', delete_album, name='delete_album'),
    path('delete_lagu/<str:id_konten>/<str:id_album>', delete_lagu, name='delete_lagu'),
]