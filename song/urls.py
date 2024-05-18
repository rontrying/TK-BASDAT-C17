from django.urls import path
from .views import *
app_name = 'song'

urlpatterns = [
    path('details/<uuid:id_konten>/', song_details, name='song_details'),
    path('tambah-lagu/<uuid:id_konten>/', tambah_lagu_ke_playlist, name='tambah_lagu_ke_playlist'),
]