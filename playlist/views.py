from django.shortcuts import render
from django.db import connection
from playlist.query import *
from utils import parse

def user_playlist(request):

    playlists_data = [
        {"title": "Amazing Grace", "num_songs": 0, "total_duration": "0 minute"},
        {"title": "Yellow Mellow", "num_songs": 15, "total_duration": "1 hour 15 minutes"},
        {"title": "Chill Vibes", "num_songs": 3, "total_duration": "12 minutes"},
        {"title": "Galau Parah", "num_songs": 18, "total_duration": "1 hour 30 minutes"},
        {"title": "Rock Abiezzz", "num_songs": 9, "total_duration": "30 minutes"}
    ]

    playlist_dict = {
        "user": dict(request.session)
    }  
    playlist_dict["playlists"] = playlists_data
    return render(request, 'kelola_playlist.html', context = playlist_dict)

def tambah_playlist(request):
    context = {
        "user": dict(request.session)
    }
    return render(request, 'tambah_playlist.html', context)

def playlist_details(request):
    songs = [
        {"title": "Right Here", "artist": "Keshi", "duration": "3 minutes"},
        {"title": "Fragile", "artist": "Laufey", "duration": "5 minutes"},
        {"title": "Katakan Saja", "artist": "Adikara", "duration": "4 minutes"}
    ]

    playlist = {
        "title": "Chill Vibes",
        "num_songs": 3,
        "total_duration": "12 minutes",
        "creation_date": "04/04/2024",
        "description": "Little chill in your home!",
        "songs": songs
    }

    user_email = request.session.get('email')

    with connection.cursor() as cursor:
        if request.session.get('role') == 'Label':
            query = get_label_profile(user_email)
        else:
            query = get_user_profile(user_email)

        cursor.execute(query)
        result = parse(cursor)

    context = result[0]

    context["playlist"] = playlist

    context["user"] = dict(request.session)

    return render(request, 'playlist_details.html', context)

def tambah_lagu(request):

    all_songs = [
        {"id": 1, "title": "As It Was", "artist": "Harry Styles"},
        {"id": 2, "title": "About Damn Time", "artist": "Lizzo"},
        {"id": 3, "title": "First Class", "artist": "Jack Harlow"},
        {"id": 4, "title": "Wait For U", "artist": "Future featuring Drake & Tems"},
        {"id": 5, "title": "Me Porto Bonito", "artist": "Bad Bunny & Chencho Corleone"},
        {"id": 6, "title": "Moscow Mule", "artist": "Bad Bunny"},
        {"id": 7, "title": "Tití Me Preguntó", "artist": "Bad Bunny"},
        {"id": 8, "title": "Running Up That Hill", "artist": "Kate Bush"},
        {"id": 9, "title": "The Kind Of Love We Make", "artist": "Luke Combs"},
        {"id": 10, "title": "I Ain't Worried", "artist": "OneRepublic"}
    ]

    context = {
        "all_songs": all_songs
    }
    context["user"] = dict(request.session)
    return render(request, 'tambah_lagu.html', context)

def update_playlist(request):
    context = {
        "user": dict(request.session)
    }
    return render(request, 'update_playlist.html', context)