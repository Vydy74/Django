from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.name

