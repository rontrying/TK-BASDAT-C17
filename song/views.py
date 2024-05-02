from django.shortcuts import render

def song_details(request):
    song = {
        "title": "Right Here",
        "genres": ["Pop", "Indie"],
        "artist": "Keshi",
        "songwriters": ["Keshi", "Kenji"], 
        "duration": "3 menit",
        "release_date": "24/09/19",
        "year": 2019,
        "total_plays": 100000,
        "total_downloads": 1000,
        "album": "bandaids",
    }

    context = {
        "song": song
    }

    return render(request, 'song_details.html', context)