from django.shortcuts import render
from django.db import connection
from album_and_song.query import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
import uuid
import ast
# Create your views here.

@csrf_exempt
def create_album(request):
    context = {}
    cursor = connection.cursor()
    cursor.execute(select_label())
    result = cursor.fetchall()
    context["data"] = result
    user_email = request.session.get("email")
    context["user"] = dict(request.session)
    if request.session.get("is_artist"):
        query = get_id_artist(user_email)
    else:
        query = get_id_songwriter(user_email)
    
    cursor.execute(query)
    request.session["id_album_song"] = str(cursor.fetchall()[0][0])
    user_email = request.session.get("email")
    cursor.execute(get_nama(user_email))
    context["nama"] = cursor.fetchall()[0][0]
    context["user"] = dict(request.session)
    if context["user"]["is_songwriter"] and not context["user"]["is_artist"]:
        cursor.execute(select_artist())
        res = cursor.fetchall()
        context["data_artist"] = res
    elif context["user"]["is_artist"] and not context["user"]["is_songwriter"]:
        cursor.execute(select_songwriter())
        res = cursor.fetchall()
        context["data_songwriter"] = res
    else :
        pass  # gaperlu fetch data karena label nama dan songwriter
    print(context)
    cursor.execute(select_genre())
    context["genre"] = cursor.fetchall()
    if request.method == "POST":
        id_album = uuid.uuid4()
        id_label = request.POST.get("label")
        title = request.POST.get("title")
        str_id_album = str(id_album)
        id_konten = uuid.uuid4()
        str_id_konten = str(id_konten)
        if context["user"]["is_songwriter"] :
            id_songwriter = request.session["id_album_song"]
            id_artist = request.POST.get("artist")
        else :
            id_artist = request.session["id_album_song"]
            list_id_songwriter= request.POST.getlist("selected-songwriter")
            id_songwriter_list = ast.literal_eval(str(list_id_songwriter))
            id_songwriter_list = id_songwriter_list[0].split(',')
        list_genre = request.POST.getlist("selected-genre")
        durasi = request.POST.get("duration")
        cursor.execute(insert_new_album(str_id_album,title,0,id_label,0))
        cursor.execute(insert_new_konten(str_id_konten,title,durasi))
        genre_list = ast.literal_eval(str(list_genre))
        genre_list = genre_list[0].split(',')
        for x in genre_list:
            cursor.execute(insert_konten_genre(str_id_konten,x))
        cursor.execute(insert_song(str_id_konten,str(id_artist),str_id_album))
        if context["user"]["is_songwriter"] :
            cursor.execute(insert_songwriter_write_song(id_songwriter,id_konten))
        else :
            for x in id_songwriter_list:
                cursor.execute(insert_songwriter_write_song(x,id_konten))
        print(title,id_artist,durasi,list_genre)
        return redirect("album_and_song:list_album")
    return render(request, "create_album.html", context=context)

def delete_album(request,id_album):
    cursor = connection.cursor()
    cursor.execute(album_delete(id_album))
    return HttpResponseRedirect(reverse("album_and_song:list_album"))

def delete_lagu(request,id_konten,id_album):
    cursor = connection.cursor()
    cursor.execute(lagu_delete(id_konten))
    return HttpResponseRedirect(reverse("album_and_song:daftar_lagu",args=[id_album]))

def list_album(request):
    context = {}
    cursor = connection.cursor()
    context["user"] = dict(request.session)
    if context["user"]["is_artist"] and not context["user"]["is_songwriter"]:
        user_id = request.session["id_album_song"]
        query = select_album_artist_songwriter(user_id)
        cursor.execute(query)
        result = cursor.fetchall()
    elif context["user"]["is_artist"]:
        user_id = request.session["id_album_song"]
        query = select_album_artist(user_id)
        cursor.execute(query)
        result = cursor.fetchall()
    elif context["user"]["is_songwriter"]:
        user_id = request.session["id_album_song"]
        query = select_album_songwriter(user_id)
        cursor.execute(query)
        result = cursor.fetchall()
    else :
        user_email = request.session.get("email")
        query = select_album_label(user_email)
        cursor.execute(query)
        result = cursor.fetchall()
    context["user"] = dict(request.session)
    context["data"] = result
    print(context)
    return render(request, "list_album.html", context=context)


@csrf_exempt
def create_lagu(request, id_album=""):
    context={}
    cursor = connection.cursor()
    cursor.execute(select_nama_album(id_album))
    nama_album = cursor.fetchall()[0][0]
    context = {"nama_album": nama_album}
    user_email = request.session.get("email")
    cursor.execute(get_nama(user_email))
    context["nama"] = cursor.fetchall()[0][0]
    context["user"] = dict(request.session)
    if context["user"]["is_songwriter"] and not context["user"]["is_artist"]:
        cursor.execute(select_artist())
        res = cursor.fetchall()
        context["data_artist"] = res
    elif context["user"]["is_artist"] and not context["user"]["is_songwriter"]:
        cursor.execute(select_songwriter())
        res = cursor.fetchall()
        context["data_songwriter"] = res
    else :
        pass  # gaperlu fetch data karena label nama dan songwriter
    cursor.execute(select_genre())
    context["genre"] = cursor.fetchall()
    if request.method == "POST":
        title = request.POST.get("title")
        str_id_album = str(id_album)
        id_konten = uuid.uuid4()
        str_id_konten = str(id_konten)
        if context["user"]["is_songwriter"] :
            id_songwriter = request.session["id_album_song"]
            id_artist = request.POST.get("artist")
        else :
            id_artist = request.session["id_album_song"]
            list_id_songwriter= request.POST.getlist("selected-songwriter")
            id_songwriter_list = ast.literal_eval(str(list_id_songwriter))
            id_songwriter_list = id_songwriter_list[0].split(',')
        list_genre = request.POST.getlist("selected-genre")
        durasi = request.POST.get("duration")
        cursor.execute(insert_new_konten(str_id_konten,title,durasi))
        genre_list = ast.literal_eval(str(list_genre))
        genre_list = genre_list[0].split(',')
        for x in genre_list:
            cursor.execute(insert_konten_genre(str_id_konten,x))
        cursor.execute(insert_song(str_id_konten,str(id_artist),str_id_album))
        if context["user"]["is_songwriter"] :
            cursor.execute(insert_songwriter_write_song(id_songwriter,id_konten))
        else :
            for x in id_songwriter_list:
                cursor.execute(insert_songwriter_write_song(x,id_konten))
        print(title,id_artist,durasi,list_genre)
        return redirect("album_and_song:daftar_lagu",id_album=str(id_album))
    return render(request, "create_lagu.html", context=context)

@csrf_exempt
def daftar_lagu(request, id_album=""):
    with connection.cursor() as cursor:
        cursor.execute(select_nama_album(id_album))
        nama_album = cursor.fetchall()[0][0]
    context = {"nama_album": nama_album}
    with connection.cursor() as cursor:
        cursor.execute(select_lagu(id_album))
        result = cursor.fetchall()
    context["user"] = dict(request.session)
    context["data"] = result
    context["no_album"] = id_album
    return render(request, "daftar_lagu.html", context=context)