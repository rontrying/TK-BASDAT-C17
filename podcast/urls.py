from django.urls import path
from podcast.views import *

urlpatterns = [
    path('', play_podcast, name='podcast'),
]