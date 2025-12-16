from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from .models import Flight, Country

def flights_page(request):

    flights_list = Flight.objects.all()
    country_list = Country.objects.all()
    context = {
        'flights_list': flights_list,
        'country_list': country_list
    }

    return render(request, "flights.html", context)

def register_view(request):
    context = {
        'error': []
    }

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if username and password and confirm and password == confirm:
            user_from_db = authenticate(request, username=username, password=password)

            if user_from_db is None:
                User.objects.create(
                    username=username,
                    password=make_password(password)
                )
                return redirect('login')
            else:
                context['error'].append('Ошибка! Пользователь с таким логином уже существует')
        else:
            context['error'].append('Ошибка! Введите данные правильно')

    return render(request, 'register.html', context)

def login_view(request):
    context = {'error': []
    }

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('flights_page')
        else:
            context['error'].append('Ошибка! Неверный логин или пароль.')

    return render(request, 'login.html', context)
        
def logout_view(request):
    logout(request)
    return redirect("login")