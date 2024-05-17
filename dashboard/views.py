from django.shortcuts import render
from django.db import connection
from dashboard.query import *
from utils import parse, parse_role
from dashboard.helper import *


def user_dashboard(request):
    user_email = request.session.get('email')
    is_label = request.session.get('is_label', False)

    context = {
        "song_content": [],
        "podcast_content": [],
        "playlist_content": [],
        "album_content": []
    }

    with connection.cursor() as cursor:
        if is_label:
            query, params = get_label_data(user_email)
            cursor.execute(query, params)
            label_data = parse(cursor)
            label_data = label_data[0] 
            context.update({
                    'nama': label_data.get('label_name'),
                    'kontak': label_data.get('kontak'),
                    'email': label_data.get('email'),
                    'album_content': [label_data['judul_album']] if label_data['judul_album'] else []
                })
        else:
            cursor.execute(check_subscription_status(user_email))

            query= get_user_data(user_email)
            cursor.execute(query)
            user_content = parse(cursor)
            context.update(user_content[0] if user_content else {})

            if user_content:
                context.update(parse_user_dashboard(user_content))

    context = {k: (v if v else False) for k, v in context.items()}

    user_info = dict(request.session)
    context['user'] = user_info
    context["role"] = parse_role(context["user"]["roles"])
    context['gender'] = "Male" if user_info.get('gender') == 1 else "Female"

    return render(request, 'dashboard.html', context)

