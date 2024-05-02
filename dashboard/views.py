from django.shortcuts import render
from django.db import connection
from dashboard.query import *
from utils import parse, parse_role


def user_dashboard(request):
    user_email = request.session.get('email')

    with connection.cursor() as cursor:
        if request.session.get('is_label'):
            query = get_label_profile(user_email)
        else:
            query = get_user_profile(user_email)

        cursor.execute(query)
        result = parse(cursor)

    context = result[0]
    context["user"] = dict(request.session)
    context["role"] = parse_role(context["user"]["roles"])
    if context["user"]["is_user"]:
        context["gender"] = "Male" if context["gender"] == 1 else "Female"
    print(context["user"])

    return render(request, 'dashboard.html', context)