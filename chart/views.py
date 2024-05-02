from django.shortcuts import render
from django.db import connection
from chart.query import *
from utils import parse


def chart_list(request):
    with connection.cursor() as cursor:
        query = get_chart()
        cursor.execute(query)
        result = parse(cursor)
    
    for row in result:
        row["chart_type"] = row["tipe"].replace(" ", "-").lower()
    
    context = {"chart_types": result}
    context["user"] = dict(request.session)
    
    return render(request, 'chart_list.html', context)

def chart_detail(request, chart_type):
    chart_type = chart_type.replace("-", " ").title()
    chart_details = [
        {'title': 'Song1', 'artist': 'Artist1', 'release_date': '09/03/2024', 'total_plays': 21000},
        {'title': 'Song2', 'artist': 'Artist2', 'release_date': '02/03/2024', 'total_plays': 19000}
    ]
    context = {'chart_details': chart_details, 'chart_type': chart_type}
    context["user"] = dict(request.session)
    return render(request, 'chart_detail.html', context)
