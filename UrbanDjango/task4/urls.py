from django.contrib import admin
from django.urls import path

from . import views
from task4.views import main_page_view, store_page_view, basket_page_view, contacts_page_view

app_name = 'task4'

urlpatterns = [
    path('', main_page_view),
    path('store_page/', store_page_view),
    path('basket_page/', basket_page_view),
    path('contact_page/', contacts_page_view),
]