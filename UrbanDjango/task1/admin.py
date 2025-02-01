from django.contrib import admin
from .models import Product
from .models import User

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)

@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'age')
    search_fields = ('username',)
