from django.shortcuts import render
from django.db import connection
from homepage.query import *
from utils import parse

def homepage_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM akun")
        result = cursor.fetchall()
    
    return render(request, 'index.html', {'data': result})
