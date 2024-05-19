from django.urls import path
from podcast.views import *

urlpatterns = [
    path('play/<str:podcast_id>/', play_podcast, name='play'),
    path('', podcast_list, name='podcast_list'),
    path('episodes/<str:podcast_id>/', episode_list, name='episode_list'),
    path('add-episode/<str:podcast_id>/', add_episode, name='add_episode'),
    path('add-podcast/', add_podcast, name='add_podcast'),
    path('delete-podcast/<str:podcast_id>/', delete_podcast, name='delete_podcast'),
    path('episodes/<str:podcast_id>/delete-episode/<str:episode_id>/', delete_episode, name='delete_episode'),
]