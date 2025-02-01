from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import main_page_view, store_page_view, basket_page_view, contacts_page_view
from .views import sign_up_by_django, registration_page, base_page, login_user

app_name = 'task1'

urlpatterns = [
    path('', main_page_view, name='main_page'),
    path('store_page/', store_page_view),
    path('basket_page/', basket_page_view),
    path('contact_page/', contacts_page_view),
    path('registration/', registration_page, name='registration_page'),
    path('django_sign_up/', sign_up_by_django, name='sign_up_by_django'),
    path('login/', login_user, name='login_user'),
    path('base/', base_page, name='base')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)