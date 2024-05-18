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

    with connection.cursor() as cursor:
        cursor.execute(select_song_details(id_konten))
        song = parse(cursor)[0]
        durasi_int = song["duration"]
        song['duration'] = format_duration(durasi_int)
        song['id_konten'] = id_konten

    context = {
        "user": dict(request.session),
        "song": song,
    }

    return render(request, 'song_details.html', context)

def tambah_lagu_ke_playlist(request, id_konten):
    
    context = {
        "user": dict(request.session),
    }    

    with connection.cursor() as cursor:
        cursor.execute(select_song_details(id_konten))
        song = parse(cursor)[0]
        durasi_int = song["duration"]
        song['duration'] = format_duration(durasi_int)
        song['id_konten'] = id_konten

        cursor.execute(select_all_user_playlist(context["user"]['email']))
        playlists = parse(cursor)

    context["song"] = song
    context["playlists"] = playlists

    if (request.method == "POST"):
        return redirect("song_details", id_konten=id_konten)

    return render(request, 'tambah_lagu_ke_playlist.html', context)