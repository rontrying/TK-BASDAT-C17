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
    chart_details = []
    chart_type = chart_type.replace("-", " ").title()

    with connection.cursor() as cursor: 
        query = update_chart_detail(chart_type)
        cursor.execute(query)

        query = get_chart_detail(chart_type)
        cursor.execute(query)
        result = parse(cursor)
        for num, entry in enumerate(result):
            chart_details.append({
                "number": num + 1,
                "title": entry["judul_lagu"],
                "artist": entry["nama_penyanyi"],
                "release_date": entry["tanggal_rilis"].strftime("%d/%m/%Y"),
                "total_plays": entry["total_play"],
                "id_konten": entry["id_konten"]
            
            })
    
    context = {'chart_details': chart_details, 'chart_type': chart_type}
    context["user"] = dict(request.session)
    return render(request, 'chart_detail.html', context)
