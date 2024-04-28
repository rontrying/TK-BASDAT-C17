from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('authentication:login_user')