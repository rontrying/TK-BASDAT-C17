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
            # get label data
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
            # run the procedure to check subscription status
            cursor.execute(check_subscription_status(user_email))

            # get user data
            query, params = get_user_data(user_email)
            cursor.execute(query, params)
            user_content = parse(cursor)
            context.update(user_content[0] if user_content else {})

            context['playlist_content'] = [item['judul_playlist'] for item in user_content if item['judul_playlist'] and item["judul_playlist"] is not None]
            context['song_content'] = [item['judul'] for item in user_content if item['tipe'] == 'lagu'and item["judul"] is not None]
            context['podcast_content'] = [item['judul'] for item in user_content if item['tipe'] == 'podcast'and item["judul"] is not None]

            print(context)

    context = {k: (v if v else False) for k, v in context.items()}

    user_info = dict(request.session)
    context['user'] = user_info
    context["role"] = parse_role(context["user"]["roles"])
    context['gender'] = "Male" if user_info.get('gender') == 1 else "Female"
    

    return render(request, 'dashboard.html', context)

