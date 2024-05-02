from django.shortcuts import render
from django.db import connection
from dashboard.query import *
from utils import parse


def get_user_profile(user_email):
    user_profile = {}
    with connection.cursor() as cursor:
        dct_role = {
            "Artist": is_artist(user_email),
            "Podcaster": is_podcaster(user_email),
            "Label": is_label(user_email),
            "Songwriter": is_songwriter(user_email)
        }
        user_profile["role"] = []
        is_user_query = is_user(user_email)
        cursor.execute(is_user_query)
        if cursor.rowcount > 0:
            user_profile = parse(cursor)[0]
            user_profile["role"] = ["Pengguna Biasa"]

        for role_name, query in dct_role.items():
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                user_profile["role"].append(role_name)
    
    return user_profile

def user_dashboard(request):
    user_email = "nancyrhodes@example.org"
    content = {}

    user_profile = get_user_profile(user_email)
    
    if "Pengguna Biasa" in user_profile["role"]:
        content['user_content'] = True
    if "Artist" in user_profile["role"]:
        content['artist_content'] = True
    if "Songwriter" in user_profile["role"]:
        content['songwriter_content'] = True
    if "Podcaster" in user_profile["role"]:
        content['podcaster_content'] = True
    if "Label" in user_profile["role"]:
        content['label_content'] = True

    user_profile["role"] = ", ".join(user_profile["role"])
    user_profile["gender"] = "Male" if user_profile["gender"] == 1 else "Female"
    user_profile["content"] = content

    return render(request, 'dashboard.html', user_profile)