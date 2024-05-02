from django.shortcuts import render
from django.db import connection
from playlist.query import *
from utils import parse

def user_playlist(request):

    playlists_data = [
        {"title": "Amazing Grace", "num_songs": 0, "total_duration": "0 menit"},
        {"title": "Yellow Mellow", "num_songs": 15, "total_duration": "75 menit"},
        {"title": "Chill Vibes", "num_songs": 3, "total_duration": "12 menit"},
        {"title": "Galau Parah", "num_songs": 18, "total_duration": "90 menit"},
        {"title": "Rock Abiezzz", "num_songs": 9, "total_duration": "30 menit"}
    ]

    playlists_dict = {"playlists": playlists_data}
    return render(request, 'kelola_playlist.html', context = playlists_dict)

def tambah_playlist(request):
    return render(request, 'tambah_playlist.html', {})

def playlist_details(request):
    songs = [
        {"title": "Right Here", "artist": "Keshi", "duration": "3 menit"},
        {"title": "Fragile", "artist": "Laufey", "duration": "5 menit"},
        {"title": "Katakan Saja", "artist": "Adikara", "duration": "4 menit"}
    ]

    playlist = {
        "title": "Chill Vibes",
        "creator": "Ricardo",
        "num_songs": 3,
        "total_duration": "12 menit",
        "creation_date": "04/04/2024",
        "description": "Little chill in your home!",
        "songs": songs
    }

    context = {
        "playlist": playlist
    }

    return render(request, 'playlist_details.html', context)