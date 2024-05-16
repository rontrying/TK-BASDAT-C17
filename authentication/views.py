from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db import InternalError, connection
from authentication.query import *
from utils import parse, roles
import random

# TODO: uuid harus dibikin biar ga sama
import uuid
# Create your views here.

def registration_type(request):
    return render(request, 'registration_type.html', context={})

def register_label(request):
    form = {}
    
    context = {'form':form}
    return render(request, 'register_label.html', context)

def register_pengguna(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        with connection.cursor() as cursor:

            try:
                # Insert akun ke table
                nama = request.POST.get('name')
                gender = request.POST.get('gender')
                tempat_lahir = request.POST.get('birthplace')
                tanggal_lahir = request.POST.get('birthdate')
                podcaster = request.POST.get('role_podcaster')
                artist = request.POST.get('role_artist')
                songwriter = request.POST.get('role_songwriter')
                kota_asal = request.POST.get('city')
                cursor.execute(insert_akun(email, password, nama, int(gender), tempat_lahir,
                                           tanggal_lahir, True if (podcaster or artist or songwriter) else False, 
                                           kota_asal))
                # cursor.execute(insert_non_premium(email))
                
                # Generate id pemilik hak cipta
                id_pemilik_hak_cipta = uuid.UUID(int=random.getrandbits(128))
                if (songwriter or artist):
                    id_pemilik_hak_cipta = uuid.UUID(int=random.getrandbits(128))
                    rate_royalti = random.choice([i*50 for i in range(1, 50)])
                    while (check_pemilik_hak_cipta(cursor, id_pemilik_hak_cipta)):
                        id_pemilik_hak_cipta = uuid.UUID(int=random.getrandbits(128))
                    cursor.execute(insert_pemilik_hak_cipta(id_pemilik_hak_cipta, rate_royalti))

                # Generate id artist
                id_artist = uuid.UUID(int=random.getrandbits(128))
                if (artist):
                    while (check_artist(cursor, id_artist)):
                        id_artist = uuid.UUID(int=random.getrandbits(128))

                # Generate id songwriter
                id_songwriter = uuid.UUID(int=random.getrandbits(128))
                if (songwriter):
                    while (check_songwriter(cursor, id_songwriter)):
                        id_songwriter = uuid.UUID(int=random.getrandbits(128))
                
                # Insert akun if verified
                insert_verified(cursor, email, podcaster, artist, songwriter, 
                                id_artist, id_songwriter, id_pemilik_hak_cipta)
                return redirect('authentication:login_user')
            
            # Kalo udah ada emailnya
            except InternalError:
                messages.error(request, 'Email has been used. Please try again')
                # cursor.execute(get_nonpremium(email))
                # cursor.execute(delete_artist(email))         
                # cursor.execute(delete_podcaster(email))
                # cursor.execute(delete_songwriter(email))       
                # cursor.execute(delete_akun(email))

    return render(request, 'register_pengguna.html', context={})

def insert_verified(cursor, email, podcaster, artist, songwriter, id_artist, id_songwriter, id_pemilik_hak_cipta):
    if (podcaster):
        cursor.execute(insert_podcaster(email))
        # cursor.execute(get_podcaster(email))
        # print(parse(cursor))
    if (artist):
        cursor.execute(insert_artist(id_artist, email, id_pemilik_hak_cipta))
        # cursor.execute(get_artist(email))
        # print(parse(cursor))
    if (songwriter):
        cursor.execute(insert_songwriter(id_songwriter, email, id_pemilik_hak_cipta))
        # cursor.execute(get_podcaster(email))
        # print(parse(cursor))
    return
    
def check_pemilik_hak_cipta(cursor, id):
    cursor.execute(get_pemilik_hak_cipta(id))
    result = parse(cursor)
    return False if len(result) == 0 else True

def check_artist(cursor, id):
    cursor.execute(get_artist_by_id(id))
    result = parse(cursor)
    return False if len(result) == 0 else True

def check_songwriter(cursor, id):
    cursor.execute(get_songwriter_by_id(id))
    result = parse(cursor)
    return False if len(result) == 0 else True

def login_user(request):
    request.session["is_user"] = False
    request.session["is_label"] = False
    request.session["is_artist"] = False
    request.session["is_premium"] = False
    request.session["is_podcaster"] = False
    request.session["is_songwriter"] = False

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        with connection.cursor() as cursor:
            cursor.execute(get_user_role(email, password))
            result = parse(cursor)
            if len(result) > 0:
                for row in result:
                    request.session[roles[row['role']]] = True

                if request.session["is_user"] or request.session["is_label"]:
                    request.session["roles"] = [role for role, value in request.session.items() if value == True
                                                and role != "is_authenticated"]
                    request.session["is_authenticated"] = True
                    request.session["email"] = email
                    return redirect('dashboard')
                else:
                    messages.info(request, 'Incorrect username or password. Please try again')
            else:
                messages.info(request, 'Incorrect username or password. Please try again')

    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    # clear session
    request.session.clear()
    logout(request)
    return redirect('authentication:login_user')