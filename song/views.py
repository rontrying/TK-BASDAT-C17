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
from django.http import JsonResponse


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

def add_song_to_playlist(request, id_konten):
    if request.method == "POST":
        selected_playlist_id = request.POST.get('selectedPlaylistId')

        if selected_playlist_id:
            with connection.cursor() as cursor:
                cursor.execute(select_song_details(id_konten))
                song = parse(cursor)[0]
                id_song = id_konten
                
                cursor.execute(check_playlist_song(selected_playlist_id, id_song))
                result = parse(cursor)
                cursor.execute(select_user_playlist_by_root_id(selected_playlist_id))
                playlist = parse(cursor)[0]
                playlist_title = playlist['judul']
                id_user_playlist = playlist['id_user_playlist']

                if len(result) != 1:
                    cursor.execute(insert_playlist_song(selected_playlist_id, id_song))
                    return JsonResponse({'success': True, 'playlist_id': selected_playlist_id, 'song_title': song['title'], 'playlist_title': playlist_title, 'id_user_playlist': id_user_playlist})
                else:
                    return JsonResponse({'success': False, 'playlist_id': selected_playlist_id, 'song_title': song['title'], 'playlist_title': playlist_title, 'id_user_playlist': id_user_playlist})
        return JsonResponse({'success': False, 'message': 'Playlist not selected'})

def tambah_lagu_ke_playlist(request, id_konten):
    context = {
        "user": dict(request.session),
        "success": None,
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

    if "success" in request.GET:
        context["success"] = request.GET["success"] == "True"

    return render(request, 'tambah_lagu_ke_playlist.html', context)

@csrf_exempt
def download_song(request, id_konten):
    if request.method == "POST":
        user = dict(request.session)
        email_downloader = user['email']
        
        with connection.cursor() as cursor:
            cursor.execute(select_song_details(id_konten))
            song = parse(cursor)[0]
            id_song = id_konten

            try:
                cursor.execute(insert_song_to_downloaded_song(id_song, email_downloader))
                cursor.execute(update_download(id_song))
                return JsonResponse({'success': True, 'song_title': song['title'], 'already_downloaded': False})
            except InternalError as e:
                if 'already downloaded' in str(e):
                    cursor.execute(select_one_playlist(id_song, email_downloader))
                    playlist = parse(cursor)
                    cursor.execute(update_download(id_song))

                    if len(playlist) == 0:
                        return JsonResponse({'success': True, 'song_title': song['title'], 'already_downloaded': True, 'id_user_playlist': ""})
                    else:
                        return JsonResponse({'success': True, 'song_title': song['title'], 'already_downloaded': True, 'id_user_playlist': playlist[0]['id_user_playlist']})
                else:
                    return JsonResponse({'success': False, 'message': 'An error occurred'})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@csrf_exempt
def shuffle_play(request, id_user_playlist):
    if request.method == 'POST':
        user = dict(request.session)
        email_pemain = user['email']
        with connection.cursor() as cursor:
            cursor.execute(select_user_playlist_by_id(id_user_playlist))
            user_playlist = parse(cursor)[0]
            cursor.execute(get_songs(id_user_playlist))
            songs = parse(cursor)

            if (user_playlist['jumlah_lagu'] == 0):
                return JsonResponse({'success': True, 'message': "You don't have a song"})
            
            email_pembuat = user_playlist['email_pembuat']
            cursor.execute(insert_akun_play_user_playlist(email_pemain, id_user_playlist, email_pembuat))

            cursor.execute(get_songs(id_user_playlist))
            songs = parse(cursor)
            for song in songs:
                play_song_in_playlist(request, song['id'])
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@csrf_exempt
def play_song(request, id_konten):
    if request.method == "POST":
        user = dict(request.session)
        email_pemain = user['email']
        progress = request.POST.get('progress', 0)

        if float(progress) > 70:
            with connection.cursor() as cursor:
                cursor.execute(insert_akun_play_song(email_pemain, id_konten))
                cursor.execute(update_akun_play_song(id_konten))
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Progress less than 70%'})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})


@csrf_exempt
def play_song_in_playlist(request, id_konten):
    if request.method == "POST":
        user = dict(request.session)
        email_pemain = user['email']
        with connection.cursor() as cursor:
            cursor.execute(insert_akun_play_song(email_pemain, id_konten))
            cursor.execute(update_akun_play_song(id_konten))
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})