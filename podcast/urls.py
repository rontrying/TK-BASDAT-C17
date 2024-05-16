from django.urls import path
from podcast.views import *

urlpatterns = [
    path('play/<str:podcast_id>', play_podcast, name='podcast'),
    path('', podcast_list, name='podcast_list'),
    path('episodes/', episode_list, name='episode_list'),
    path('add-episode/', add_episode, name='add_episode'),
    path('add-podcast/', add_podcast, name='add_podcast'),
    path('delete/<int:pk>/', delete_podcast, name='delete_item'),
]