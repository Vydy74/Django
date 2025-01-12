from django.shortcuts import render

def main_page_view(request):
    return render(request, 'third_task/main_page.html')

def store_page_view(request):
    return render(request, 'third_task/store_page.html')

def basket_page_view(request):
    return render(request, 'third_task/basket_page.html')

def contacts_page_view(request):
    return render(request, 'third_task/contact_page.html')
