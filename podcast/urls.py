from django.urls import path
from podcast.views import *

urlpatterns = [
    path('', play_podcast, name='podcast'),
    path('list/', podcast_list, name='podcast_list'),
    path('list/episodes/', episode_list, name='episode_list'),
    path('list/add-episode/', add_episode, name='add_episode'),
    path('list/add-podcast/', add_podcast, name='add_podcast'),
    path('list/delete/<int:pk>/', delete_podcast, name='delete_item'),
]