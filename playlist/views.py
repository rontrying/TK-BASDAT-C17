import random
import uuid
from django.shortcuts import render
from django.db import connection
from playlist.query import *
from utils import parse

def user_playlist(request):

    # playlists_data = [
    #     {"title": "Amazing Grace", "num_songs": 0, "total_duration": "0 minute"},
    #     {"title": "Yellow Mellow", "num_songs": 15, "total_duration": "1 hour 15 minutes"},
    #     {"title": "Chill Vibes", "num_songs": 3, "total_duration": "12 minutes"},
    #     {"title": "Galau Parah", "num_songs": 18, "total_duration": "1 hour 30 minutes"},
    #     {"title": "Rock Abiezzz", "num_songs": 9, "total_duration": "30 minutes"}
    # ]
    
    playlist_dict = {
        "user": dict(request.session)
    }

    email = request.session.get('email')
    with connection.cursor() as cursor:
        # Ambil User Playlist
        cursor.execute(select_user_playlist(email))
        result = parse(cursor)
        playlist_dict["playlists"] = result

        # Ambil Jumlah Lagu
        length = len(result)
        if (length != 0):
            for i in range(length):
                id = playlist_dict["playlists"][i]['id_user_playlist']
                cursor.execute(count_songs(id))
                result = parse(cursor)
                jumlah_lagu = result[0]['count']
                playlist_dict["playlists"][i]['jumlah_lagu'] = jumlah_lagu
                if (jumlah_lagu == 0):
                    playlist_dict["playlists"][i]['total_durasi'] = 0
    
    return render(request, 'kelola_playlist.html', playlist_dict)

def tambah_playlist(request):
    context = {
        "user": dict(request.session)
    }
    return render(request, 'tambah_playlist.html', context)

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
    print(songs)
    playlist['jumlah_lagu'] = song_count
    playlist['total_durasi'] = 0 if song_count == 0 else playlist['total_durasi']

    # songs = [
    #     {"title": "Right Here", "artist": "Keshi", "duration": "3 minutes"},
    #     {"title": "Fragile", "artist": "Laufey", "duration": "5 minutes"},
    #     {"title": "Katakan Saja", "artist": "Adikara", "duration": "4 minutes"}
    # ]

    # playlist = {
    #     "title": "Chill Vibes",
    #     "num_songs": song_count,
    #     "total_duration": "12 minutes",
    #     "creation_date": "04/04/2024",
    #     "description": "Little chill in your home!",
    #     "songs": songs
    # }

    context["playlist"] = playlist
    context['id_user_playlist'] = id_user_playlist

    return render(request, 'playlist_details.html', context)

def tambah_lagu(request, id_user_playlist):

    # all_songs = [
    #     {"id": 1, "title": "As It Was", "artist": "Harry Styles"},
    #     {"id": 2, "title": "About Damn Time", "artist": "Lizzo"},
    #     {"id": 3, "title": "First Class", "artist": "Jack Harlow"},
    #     {"id": 4, "title": "Wait For U", "artist": "Future featuring Drake & Tems"},
    #     {"id": 5, "title": "Me Porto Bonito", "artist": "Bad Bunny & Chencho Corleone"},
    #     {"id": 6, "title": "Moscow Mule", "artist": "Bad Bunny"},
    #     {"id": 7, "title": "Tití Me Preguntó", "artist": "Bad Bunny"},
    #     {"id": 8, "title": "Running Up That Hill", "artist": "Kate Bush"},
    #     {"id": 9, "title": "The Kind Of Love We Make", "artist": "Luke Combs"},
    #     {"id": 10, "title": "I Ain't Worried", "artist": "OneRepublic"}
    # ]

    with connection.cursor() as cursor:
        cursor.execute(select_all_songs())
        all_songs = parse(cursor)

    context = {
        "all_songs": all_songs
    }
    context["user"] = dict(request.session)
    return render(request, 'tambah_lagu.html', context)

def update_playlist(request, id_user_playlist):
    context = {
        "user": dict(request.session)
    }
    return render(request, 'update_playlist.html', context)