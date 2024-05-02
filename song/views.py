from django.shortcuts import render

def song_details(request):
    song = {
        "title": "Right Here",
        "genres": ["Pop", "Indie"],
        "artist": "Keshi",
        "songwriters": ["Keshi", "Kenji"], 
        "duration": "3 minutes",
        "release_date": "24/09/19",
        "year": 2019,
        "total_plays": 100000,
        "total_downloads": 1000,
        "album": "bandaids",
    }

    context = {
        "song": song,
        "user": dict(request.session),
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