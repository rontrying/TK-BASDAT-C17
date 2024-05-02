from django.shortcuts import render
from django.db import connection
from playlist.query import *
from utils import parse

def user_playlist(request):
    return render(request, 'kelola_playlist.html' ,context={})