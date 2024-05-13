from django.shortcuts import render
from django.db import connection
from dashboard.query import get_label_profile, get_user_profile
from utils.util import parse
from royalti.query import *

# Create your views here.
def list_royalti(request):
    context={}
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
        if context["user"]["is_songwriter"]:
            cur.execute(get_id_pemilik_hak_cipta(user_email,"songwriter"))
            id_pemilik = cur.fetchall()[0][0]
        elif context['user']['is_artist']:
            cur.execute(get_id_pemilik_hak_cipta(user_email,"artist"))
            id_pemilik = cur.fetchall()[0][0]
        else :
            cur.execute(get_id_pemilik_hak_cipta(user_email,'label'))
            id_pemilik = cur.fetchall()[0][0]
        cur.execute(get_list_royalti(id_pemilik))
        context["data"] = cur.fetchall()
    
    return render(request, 'list_royalti.html',context=context)