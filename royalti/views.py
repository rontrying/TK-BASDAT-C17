from django.shortcuts import render
from django.db import connection
from royalti.query import *

# Create your views here.
def list_royalti(request):
    context={}
    context["user"] = dict(request.session)
    user_email = request.session.get("email")
    with connection.cursor() as cur:
        if context["user"]["is_songwriter"]:
            query = get_list_royalti_songwriter(user_email)
            cur.execute(query)
        elif context['user']['is_artist']:
            query = get_list_royalti_artist(user_email)
            cur.execute(query)
        else :
            query = get_list_royalti_label(user_email)
            cur.execute(query)
        context["data"] = cur.fetchall()
    
    return render(request, 'list_royalti.html',context=context)