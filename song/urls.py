from django.urls import path
from .views import *
app_name = 'song'

urlpatterns = [
    path('details/', song_details, name='song_details'),
    path('tambah-lagu/', tambah_lagu_ke_playlist, name='tambah_lagu_ke_playlist'),
]