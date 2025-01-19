from django.db import models
from task4.models import User

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