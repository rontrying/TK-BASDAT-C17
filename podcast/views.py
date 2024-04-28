from django.shortcuts import render
from datetime import datetime

def play_podcast(request):
    # Dummy data for the context
    context = {
        'podcast_title': "The Great Podcast",
        'podcast_genres': ["Comedy", "Education"],  # This assumes genres are in a list
        'podcaster_name': "Jane Doe",
        'total_duration': "2 jam 15 menit",  # Example total duration
        'release_date': "18/03/2024",
        'year': "2024",
        'episodes': [
            {
                'title': "Episode 1: The Beginning",
                'description': "In this episode, we explore the beginnings of something great.",
                'duration': "45 menit",
                'date': "18/03/2024",
            },
            {
                'title': "Episode 2: The Continuation",
                'description': "Diving deeper into the subject, we uncover new insights.",
                'duration': "1 jam 30 menit",
                'date': "25/03/2024",
            },
        ],
    }

    return render(request, 'play_podcast.html', context)