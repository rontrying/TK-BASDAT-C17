from django.shortcuts import render
from django.db import connection
from album_and_song.query import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
# Create your views here.

@csrf_exempt
def show_main(request):
    with connection.cursor() as cursor:
        cursor.execute(select_all())
        result = cursor.fetchall()
    if request.method == "POST":
        title = request.POST.get('title')
        label = request.POST.get('label')
        return redirect("album_and_song:list_album")
    return render(request, 'create_album.html', {'data': result})

def list_album(request):
    context = {
        'user_role': "Label"
    }
    return render(request, 'list_album.html',context=context)

def create_lagu(request):
    return render(request, 'create_lagu.html')

def daftar_lagu(request):
    return render(request, 'daftar_lagu.html')