from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from .forms import UserRegister
from .models import User, Product
import logging

# Create your views here.

logger = logging.getLogger(__name__)

def main_page_view(request):
    return render(request, 'fourth_task/main_page.html')

def store_page_view(request):
    products = Product.objects.all()
    return render(request, 'fourth_task/store_page.html', {"products": products})

def basket_page_view(request):
    products = Product.objects.all()
    return render(request, 'fourth_task/basket_page.html', {"products": products})


def contacts_page_view(request):
    return render(request, 'fourth_task/contact_page.html')


def registration_page(request):
    return render(request, 'fifth_task/registration_page.html')

def sign_up_by_django(request):
    info = {}
    form = UserRegister(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            age = form.cleaned_data.get("age")
            email = request.POST.get("email")

            logger.debug(f"Received registration data: username={username}, age={age}, email={email}")

            if User.objects.filter(username=username).exists():
                info['error'] = 'Пользователь уже существует'
            elif User.objects.filter(email=email).exists():
                info['error'] = 'Этот адрес электронной почты уже зарегистрирован'
            else:
                User.objects.create(username=username, password=make_password(password), age=age, email=email)
                logger.info(f"User {username} registered successfully")
                request.session['user_info'] = {
                    'username': username,
                    'age': age,
                    'email': email
                }
                return redirect('/base/')
        else:
            logger.debug(f"Form errors: {form.errors}")
            info['error'] = 'Форма заполнена неверно'


    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', {'info': info})

def login_user(request):
    info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
            if user.password == password:
                return HttpResponse(f"Добро пожаловать, {username}!")
            else:
                info['error'] = 'Неверный пароль'
        except User.DoesNotExist:
            info['error'] = 'Пользователь не найден'

    return render(request, 'fifth_task/registration_page.html', {'info': info})

def base_page(request):
    user_info = request.session.get('user_info', None)
    return render(request, 'fifth_task/base.html', {'user_info': user_info})
