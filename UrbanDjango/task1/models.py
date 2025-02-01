from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Хранить пароли в зашифрованном виде
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.username

    def __int__(self):
        return self.age

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="buyer")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Баланс")


    @property
    def name(self):
        return self.user.username

    @property
    def user_age(self):
        return self.user.age

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    size = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Колличество")
    description = models.TextField(verbose_name="Описание")
    age_limited = models.BooleanField(default=False, verbose_name="Ограничение возраста")
    buyer = models.ManyToManyField(Buyer, related_name="items", blank=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.name


