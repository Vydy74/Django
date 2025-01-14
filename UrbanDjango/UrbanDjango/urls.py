"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from task2.views import function_base_view, ClassBaseView
from task3.views import main_page_view, store_page_view, basket_page_view, contacts_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/', function_base_view),
    path('classes/', ClassBaseView.as_view()),
    # path('task3/', main_page_view),
    # path('store_page/', store_page_view),
    # path('basket_page/', basket_page_view),
    # path('contact_page/', contacts_page_view),
    path('', include('task4.urls', namespace='task4'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
