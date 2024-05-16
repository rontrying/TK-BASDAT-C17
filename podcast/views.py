import uuid
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
    context, podcasts = {}, []
    email_account = request.session.get('email')

    with connection.cursor() as cursor:
        query = get_podcast_list(email_account)  
        cursor.execute(query)
        result = parse(cursor) 
        
        for entry in result:
            podcasts.append({
                'title': entry['judul'],  
                'podcast_id': entry['podcast_id'],
                'episode_count': entry['total_episode'],
                'total_duration': convert_minutes_to_hours(entry['total_durasi'])  
            })

    genres = ['Comedy', 'News', 'History', 'Technology', 'Sports', 'Music', 'Education', 'Health', 'Science', 'True Crime']
    context.update({'genres': genres, 'podcasts': podcasts})
    context["user"] = dict(request.session)  
    return render(request, 'podcast_list.html', context)

def episode_list(request, podcast_id):
    context, episodes = {}, []

    with connection.cursor() as cursor:
        query = get_episode_list(podcast_id=podcast_id)
        cursor.execute(query)
        result = parse(cursor)
        context["podcast_name"] = result[0]["judul_podcast"]
        if result[0]["episode_id"] != None:
            for entry in result:
                episodes.append({
                    'episode_id': entry['episode_id'],
                    'podcast_id': entry['podcast_id'],
                    'title': entry['judul'],
                    'description': entry['deskripsi'],
                    'duration': convert_minutes_to_hours(entry['durasi']),
                    'release_date': entry['tanggal_rilis'].strftime("%d/%m/%Y")
                })
            
    context.update({'episodes': episodes})
    context["user"] = dict(request.session)
    return render(request, 'episode_list.html', context)

@csrf_exempt
def add_podcast(request):
    if request.method == 'POST':
        year = datetime.now().year
        new_uuid = str(uuid.uuid4())
        title = request.POST.get('title')
        genres = request.POST.getlist('genre[]')
        duration = request.POST.get('duration')
        release_date = datetime.now().strftime("%Y-%m-%d")

        with connection.cursor() as cursor:
            cursor.execute(insert_podcast_to_konten(new_uuid, title, release_date, year, duration))
            cursor.execute(insert_podcast_to_podcast(new_uuid, request.session.get('email')))
            for genre in genres:
                cursor.execute(insert_podcast_to_genre(new_uuid, genre))
        
        return redirect('podcast_list')
    else:
        return HttpResponseNotAllowed(['POST'])
    
@csrf_exempt
def add_episode(request, podcast_id):
    print("JIDJAIWJDIWI")
    if request.method == 'POST':
        new_uuid = str(uuid.uuid4())
        title = request.POST.get('title')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        release_date = datetime.now().strftime("%Y-%m-%d")

        with connection.cursor() as cursor:
            cursor.execute(insert_episode(new_uuid, podcast_id, title, description, duration, release_date))
        
        return redirect('podcast_list')
    else:
        return HttpResponseNotAllowed(['POST'])

def delete_podcast(request, podcast_id):
    with connection.cursor() as cursor:
        cursor.execute(delete_podcast_from_genre(podcast_id))
        cursor.execute(delete_podcast_from_podcast(podcast_id))
        cursor.execute(delete_podcast_from_konten(podcast_id))

    return redirect('podcast_list')

def delete_episode(request, podcast_id, episode_id):
    with connection.cursor() as cursor:
        cursor.execute(delete_episode_from_episode(episode_id))

    return redirect('episode_list', podcast_id=podcast_id)