from django.shortcuts import render
from .models import Product

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