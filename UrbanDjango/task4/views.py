from django.shortcuts import render, redirect
from .models import Product
from django.http import HttpResponse
from .forms import UserRegister
from .models import User
import logging

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

# def registration_page(request):
#     return render(request, 'fifth_task/registration_page.html')

# users = ["user1", "user2", "user3"]  # Псевдо-список существующих пользователей

# def sign_up_by_html(request):
#     info = {}
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         repeat_password = request.POST.get("repeat_password")
#         age = request.POST.get("age")
#         email = request.POST.get("email")
#
#         if password != repeat_password:
#             info['error'] = 'Пароли не совпадают'
#         elif int(age) < 18:
#             info['error'] = 'Вы должны быть старше 18'
#         elif User.objects.filter(username=username).exists():
#             info['error'] = 'Пользователь уже существует'
#         elif User.objects.filter(email=email).exists():
#             info['error'] = 'Этот адрес электронной почты уже зарегистрирован'
#         else:
#             User.objects.create(username=username, password=password, age=age, email=email)
#             return HttpResponse(f"Приветствуем, {username}!")
#
#     return render(request, 'fifth_task/registration_page.html', {'info': info})
#


# def sign_up_by_django(request):
#     info = {}
#     form = UserRegister(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             age = form.cleaned_data.get("age")
#             email = request.POST.get("email")
#
#
#             if User.objects.filter(username=username).exists():
#                 info['error'] = 'Пользователь уже существует'
#             elif User.objects.filter(email=email).exists():
#                 info['error'] = 'Этот адрес электронной почты уже зарегистрирован'
#             else:
#                 User.objects.create(username=username, password=password, age=age, email=email)
#                 return HttpResponse(f"Приветствуем, {username}!")
#
#
#     info['form'] = form
#     return render(request, 'fifth_task/registration_page.html', {'info': info})
#
# def login_user(request):
#     info = {}
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#
#         try:
#             user = User.objects.get(username=username)
#             if user.password == password:
#                 return HttpResponse(f"Добро пожаловать, {username}!")
#             else:
#                 info['error'] = 'Неверный пароль'
#         except User.DoesNotExist:
#             info['error'] = 'Пользователь не найден'
#
#     return render(request, 'fifth_task/registration_page.html', {'info': info})