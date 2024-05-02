from datetime import datetime
from django.urls import reverse
from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt


def play_podcast(request):
    context = {
        'podcast_title': "The Great Podcast",
        'podcast_genres': ["Comedy", "Education"],  
        'podcaster_name': "Jane Doe",
        'total_duration': "2 jam 15 menit",  
        'release_date': "18/03/2024",
        'year': "2024",
        'episodes': [
            {
                'title': "Episode 1: The Beginning",
                'description': "In this episode, we explore the beginnings of something great.",
                'duration': "45 minutes",
                'date': "18/03/2024",
            },
            {
                'title': "Episode 2: The Continuation",
                'description': "Diving deeper into the subject, we uncover new insights.",
                'duration': "1 hour 30 minutes",
                'date': "25/03/2024",
            },
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