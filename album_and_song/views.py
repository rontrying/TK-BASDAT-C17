from django.shortcuts import render
from django.db import connection
from album_and_song.query import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

@csrf_exempt
def create_album(request):
    context = {}
    with connection.cursor() as cursor:
        cursor.execute(select_all())
        result = cursor.fetchall()
    if request.method == "POST":
        title = request.POST.get('title')
        label = request.POST.get('label')
        return redirect("album_and_song:list_album")
    context["user"] = dict(request.session)
    context["data"] = result
    return render(request, 'create_album.html', context=context)

def list_album(request):
    with connection.cursor() as cursor:
        cursor.execute(select_album())
        result = cursor.fetchall()
    context = {}
    context["user"] = dict(request.session)
    context["data"] = result
    return render(request, 'list_album.html',context=context)

@csrf_exempt
def create_lagu(request):
    context = {}
    context["user"] = dict(request.session)
    if request.method == "POST":
        title = request.POST.get('title')
        label = request.POST.get('label')
        redirect("album_and_song:daftar_lagu")
    return render(request, 'create_lagu.html',context=context)

def daftar_lagu(request,nama_album=""):
    context = {
        "nama_album":nama_album
    }
    with connection.cursor() as cursor:
        cursor.execute(select_lagu(nama_album))
        result = cursor.fetchall()
    context["user"] = dict(request.session)
    context["data"] = result
    return render(request, 'daftar_lagu.html',context=context)