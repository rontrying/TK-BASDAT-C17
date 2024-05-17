import random
import uuid
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.db import InternalError, connection
from django.contrib import messages  
from playlist.query import *
from utils import parse
from datetime import datetime
from django.http import HttpResponseRedirect

def user_playlist(request):
    
    playlist_dict = {
        "user": dict(request.session)
    }

    email = request.session.get('email')
    with connection.cursor() as cursor:
        # Ambil User Playlist
        cursor.execute(select_user_playlist(email))
        result = parse(cursor)
        playlist_dict["playlists"] = result
    
    return render(request, 'kelola_playlist.html', playlist_dict)

def check_user_playlist(cursor, id):
    cursor.execute(select_user_playlist_by_id(id))
    result = parse(cursor)
    return False if len(result) == 0 else True

def get_current_date(): 
    return datetime.now().strftime('%Y-%m-%d')

def check_playlist(cursor, id):
    cursor.execute(select_playlist(id))
    result = parse(cursor)
    return False if len(result) == 0 else True

@csrf_exempt
def tambah_playlist(request):
    context = {
        "user": dict(request.session),
        'playlist_created': False
    }

    if (request.method == "POST"):
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        email = request.session.get('email')

        with connection.cursor() as cursor:
            id_playlist = uuid.UUID(int=random.getrandbits(128))
            while (check_playlist(cursor, id_playlist)):
                id_playlist = uuid.UUID(int=random.getrandbits(128))
            cursor.execute(insert_playlist(id_playlist))
            
            id_user_playlist = uuid.UUID(int=random.getrandbits(128))
            while (check_user_playlist(cursor, id_user_playlist)):
                id_user_playlist = uuid.UUID(int=random.getrandbits(128))

            cursor.execute(insert_user_playlist(email, id_user_playlist, judul, deskripsi, 0, get_current_date(),
                                                id_playlist, 0))
            messages.success(request, 'Your playlist has been successfully created.\n' + \
                                      'This message will be closed automatically.')
            return redirect('user_playlist')

    return render(request, 'tambah_playlist.html', context)

@csrf_exempt
def delete_playlist(request, id_user_playlist):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute(select_user_playlist_by_id(id_user_playlist))
            result = parse(cursor)[0]
            fk_id_playlist = result['id_playlist']

            cursor.execute(delete_akun_play_user_playlist(id_user_playlist))
            cursor.execute(delete_playlist_song_query(fk_id_playlist))
            cursor.execute(delete_user_playlist_query(id_user_playlist))
            cursor.execute(delete_playlist_query(fk_id_playlist))

        messages.success(request, "Playlist deleted successfully. This message will be closed automatically.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def playlist_details(request, id_user_playlist):
    context = {
        'user': dict(request.session)
    }

    with connection.cursor() as cursor:
        cursor.execute(select_user_playlist_by_id(id_user_playlist))
        playlist = parse(cursor)[0]

        cursor.execute(get_songs(id_user_playlist))
        songs = parse(cursor)
        song_count = len(songs)
        
        cursor.execute(get_user_profile(context["user"]['email']))
        nama = parse(cursor)[0]['nama']
        context['user']['nama'] = nama
    
    playlist['songs'] = songs
    playlist['jumlah_lagu'] = song_count
    playlist['total_durasi'] = 0 if song_count == 0 else playlist['total_durasi']

    context["playlist"] = playlist
    context['id_user_playlist'] = id_user_playlist

    return render(request, 'playlist_details.html', context)

@csrf_exempt
def tambah_lagu(request, id_user_playlist):

    with connection.cursor() as cursor:
        cursor.execute(select_all_songs())
        all_songs = parse(cursor)

        cursor.execute(select_user_playlist_by_id(id_user_playlist))
        playlist = parse(cursor)[0]

    context = {
        "all_songs": all_songs,
        "playlist": playlist,
        "user": dict(request.session)
    }

    if (request.method == "POST"):
        id_song = request.POST.get('song')
        id_playlist = playlist["id_playlist"]
        with connection.cursor() as cursor:
            try:
                cursor.execute(insert_playlist_song(id_playlist, id_song))
                cursor.execute(update_user_playlist_count(id_playlist))
                cursor.execute(update_user_playlist_duration(id_playlist))
            except InternalError:
                messages.error(request, "You already added this song in the playlist! You can't add it twice!")
                return render(request, 'tambah_lagu.html', context)
        return redirect('playlist_details', id_user_playlist=id_user_playlist)
    return render(request, 'tambah_lagu.html', context)

# Asumsi kalo string kosong atau spasi dibalikin ke judul/deskripsi sebelumnya
@csrf_exempt
def update_playlist(request, id_user_playlist):
    context = {
        "user": dict(request.session)
    }
    with connection.cursor() as cursor:
        cursor.execute(select_user_playlist_by_id(id_user_playlist))
        user_playlist = parse(cursor)[0]
        context['playlist'] = user_playlist

    if (request.method == "POST"):
        with connection.cursor() as cursor:
            judul = request.POST.get('judul').strip() if request.POST.get('judul').strip() != "" else user_playlist['judul']
            deskripsi = request.POST.get('deskripsi').strip() if request.POST.get('deskripsi').strip() != "" else user_playlist['deskripsi']

            cursor.execute(set_judul_user_playlist(judul, id_user_playlist))
            cursor.execute(set_deskripsi_user_playlist(deskripsi, id_user_playlist))

            messages.success(request, "Your playlist has been updated successfully. This message will be closed automatically.")
            return redirect('user_playlist')
    return render(request, 'update_playlist.html', context)