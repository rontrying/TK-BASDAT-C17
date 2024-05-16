from utils import parse
from podcast.query import *
from datetime import datetime
from django.urls import reverse
from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseNotAllowed
from podcast.helper import convert_minutes_to_hours
from django.views.decorators.csrf import csrf_exempt


def play_podcast(request, podcast_id):
    with connection.cursor() as cursor:
        query = get_podcast_detail(podcast_id=podcast_id)
        cursor.execute(query)
        result = parse(cursor)
        print(result)

    context = {
        'podcast_title': result[0]["judul_podcast"],
        'podcast_genres': list({entry['genre'] for entry in result}),  
        'podcaster_name': result[0]['nama'],
        'total_duration': convert_minutes_to_hours(sum(entry['durasi_eps'] for entry in result)),
        'release_date': min(entry['tanggal_rilis_podcast'] for entry in result).strftime("%d/%m/%Y"),
        'year': str(result[0]['tahun']),
        'episodes': [
            {
                'title': entry['judul_eps'],
                'description': entry['deskripsi_eps'],
                'duration': convert_minutes_to_hours(entry['durasi_eps']),
                'date': entry['tanggal_rilis_eps'].strftime("%d/%m/%Y"),
            }
            for entry in result
        ],
    }
    context["user"] = dict(request.session)

    return render(request, 'play_podcast.html', context)


def podcast_list(request):
    genres = ['Comedy', 'News', 'History', 'Technology', 'Sports', 'Music', 'Education', 'Health', 'Science', 'True Crime']
    podcasts = [
        {'title': 'COACH JUSTIN, SOK TAHU SEPAK BOLA APA MEMANG BENERAN TAHU? SELESAI TUH BARANG!!', 'episode_count': 3, 'total_duration': '60 menit'},
        {'title': 'COACH JUSTIN BONGKAR DALANG DIBALIK ANJLOKNYA INDUSTRI SEPAK BOLA INDONESIA  ', 'episode_count': 2, 'total_duration': '75 menit'},
    ]
    context ={'podcasts': podcasts, 'genres':genres}
    context["user"] = dict(request.session)
    return render(request, 'podcast_list.html', context)


def episode_list(request):
    episodes = [
        {
            'title': 'The beginning of something great',
            'description': 'Lorem Ipsum ....',
            'duration': '59 menit',
            'release_date': '18/03/2024',
        },
        {
            'title': 'The continuation of greatness',
            'description': 'Lorem Ipsum ....',
            'duration': '1 jam 2 menit',
            'release_date': '25/03/2024',
        },
    ]
    context = {'episodes': episodes}
    context["user"] = dict(request.session)
    return render(request, 'episode_list.html', context)


@csrf_exempt
def add_podcast(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        duration = request.POST.get('duration')

        with connection.cursor() as cursor:
            print(title, genre, duration)
            # cursor.execute(
            #     "INSERT INTO podcasts_podcast (title, genre_id, duration) VALUES (%s, %s, %s)",
            #     [title, genre_id, duration]
            # )
        
        return redirect('podcast_list')
    else:
        return HttpResponseNotAllowed(['POST'])
    

@csrf_exempt
def add_episode(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        genre = request.POST.get('genre')

        with connection.cursor() as cursor:
            print(title, description, duration)
            # cursor.execute(
            #     "INSERT INTO podcasts_podcast (title, genre_id, duration) VALUES (%s, %s, %s)",
            #     [title, genre_id, duration]
            # )
        
        return redirect('podcast_list')
    else:
        return HttpResponseNotAllowed(['POST'])


def delete_podcast(request, pk):
    print(pk)
    return redirect('podcast_list')