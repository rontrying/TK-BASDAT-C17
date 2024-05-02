from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db import connection
from authentication.query import *
from utils import parse, roles

# TODO: uuid harus dibikin biar ga sama
import uuid
# Create your views here.

def registration_type(request):
    return render(request, 'registration_type.html', context={})

def register_pengguna(request):
    form = UserCreationForm()

    # TODO: harus handle ganti "1/0" jadi int, sama "True" jadi boolean
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('login_user')
    context = {'form':form}
    return render(request, 'register_pengguna.html', context)

def register_label(request):
    form = UserCreationForm()

    # TODO: Handle UUID
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your label has been successfully created!')
            return redirect('login_user')
    context = {'form':form}
    return render(request, 'register_label.html', context)

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