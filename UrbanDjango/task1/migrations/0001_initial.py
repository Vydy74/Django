# Generated by Django 5.1.4 on 2025-01-19 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task4', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Баланс')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='task4.user')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('size', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Колличество')),
                ('description', models.TextField(verbose_name='Описание')),
                ('age_limited', models.BooleanField(default=False, verbose_name='Ограничение возраста')),
                ('buyer', models.ManyToManyField(blank=True, related_name='items', to='task1.buyer')),
            ],
        ),
    ]
