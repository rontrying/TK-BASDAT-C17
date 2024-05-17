import random
import uuid
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.db import InternalError, connection
from django.contrib import messages  
from .query import *
from playlist.views import *
from utils import parse
from datetime import datetime
from django.http import HttpResponseRedirect

def song_details(request, id_konten):
    # song = {
    #     "title": "",
    #     "genres": ["Pop", "Indie"],
    #     "artist": "Keshi",
    #     "songwriters": ["Keshi", "Kenji"], 
    #     "duration": "3 minutes",
    #     "release_date": "24/09/19",
    #     "year": 2019,
    #     "total_plays": 100000,
    #     "total_downloads": 1000,
    #     "album": "bandaids",
    # }

    with connection.cursor() as cursor:
        cursor.execute(select_song_details(id_konten))
        song = parse(cursor)[0]
        durasi_int = song["duration"]
        song['duration'] = format_duration(durasi_int)

    context = {
        "user": dict(request.session),
        "song": song,
    }

    return render(request, 'song_details.html', context)

def tambah_lagu_ke_playlist(request):
    context = {
        "user": dict(request.session),
    }

    playlists_data = [
        {"title": "Amazing Grace", "num_songs": 0, "total_duration": "0 minute"},
        {"title": "Yellow Mellow", "num_songs": 15, "total_duration": "1 hour 15 minute"},
        {"title": "Chill Vibes", "num_songs": 3, "total_duration": "12 minutes"},
        {"title": "Galau Parah", "num_songs": 18, "total_duration": "1 hour 30 minutes"},
        {"title": "Rock Abiezzz", "num_songs": 9, "total_duration": "30 minutes"}
    ]

    context["playlists"] = playlists_data
    return render(request, 'tambah_lagu_ke_playlist.html', context)