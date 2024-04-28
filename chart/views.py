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
    
    return render(request, 'chart_list.html', {'chart_types': result})

def chart_detail(request, chart_type):
    chart_type = chart_type.replace("-", " ").title()
    chart_details = [
        {'title': 'Song1', 'artist': 'Artist1', 'release_date': '09/03/2024', 'total_plays': 21000},
        {'title': 'Song2', 'artist': 'Artist2', 'release_date': '02/03/2024', 'total_plays': 19000}
    ]
    return render(request, 'chart_detail.html', {'chart_details': chart_details, 'chart_type': chart_type})
