from django.shortcuts import render
from django.db import connection
from album_and_song.query import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from utils import parse
from dashboard.query import get_user_profile, get_label_profile

# Create your views here.

@csrf_exempt
def create_album(request):
    context = {}
    with connection.cursor() as cursor:
        cursor.execute(select_all())
        result = cursor.fetchall()
    if request.method == "POST":
        title = request.POST.get("title")
        label = request.POST.get("label")
        return redirect("album_and_song:list_album")
    context["user"] = dict(request.session)
    context["data"] = result
    return render(request, "create_album.html", context=context)


def list_album(request):
    with connection.cursor() as cursor:
        cursor.execute(select_album())
        result = cursor.fetchall()
    context = {}
    context["user"] = dict(request.session)
    context["data"] = result
    return render(request, "list_album.html", context=context)


@csrf_exempt
def create_lagu(request, nama_album=""):
    context = {"nama_album": nama_album}
    user_email = request.session.get("email")

    with connection.cursor() as cursor:
        if request.session.get("is_label"):
            query = get_label_profile(user_email)
        else:
            query = get_user_profile(user_email)

        cursor.execute(query)
        result = parse(cursor)

    context.update(result[0])
    context["user"] = dict(request.session)
    with connection.cursor() as cur:
        if context["user"]["is_songwriter"] and not context["user"]["is_artist"]:
            cur.execute(select_artist())
            res = cur.fetchall()
            context["data_artist"] = res
        elif context["user"]["is_artist"] and not context["user"]["is_songwriter"]:
            cur.execute(select_songwriter())
            res = cur.fetchall()
            context["data_songwriter"] = res
        elif context["user"]["is_artist"] and context["user"]["is_songwriter"]:
            pass  # gaperlu fetch data
        else:
            cur.execute(select_artist())
            res = cur.fetchall()
            context["data_artist"] = res
            cur.execute(select_songwriter())
            res = cur.fetchall()
            context["data_songwriter"] = res
    if request.method == "POST":
        title = request.POST.get("title")
        label = request.POST.get("label")
        redirect("album_and_song:daftar_lagu")
    return render(request, "create_lagu.html", context=context)


def daftar_lagu(request, nama_album=""):
    context = {"nama_album": nama_album}
    with connection.cursor() as cursor:
        cursor.execute(select_lagu(nama_album))
        result = cursor.fetchall()
    context["user"] = dict(request.session)
    context["data"] = result
    return render(request, "daftar_lagu.html", context=context)
