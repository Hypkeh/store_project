from django.db import models
import random
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    date_of_manufature = models.DateTimeField(auto_now_add=True)
    expires = models.PositiveIntegerField() #months
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images', null=True, blank=True)


class Profile(models.Model):
    USER_TYPE = (
        ('admin', 'Администратор'),
        ('buyer', 'Покупатель')
    )

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE, default='buyer')
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE)


class Category(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    PRODUCT_CATEGORIES = (
        ('Dairy', 'Молочные продукты'),
        ('Bread', 'Хлебные изделия'),
        ('Meat', 'Мясные продукты'),
        ('Fish/Seafood', 'Морепродукты'),
        ('Drinks', 'Напитки'),
        ('Snacks', 'Закуски, снеки'),
        ('Tea/Coffee', 'Кофе/Чай'),
        ('Species/Sauces', 'Специи/Соусы'),
        ('Ceareals', 'Хлопья/Крупы'),
    )
    category = models.CharField(max_length=20, choices=PRODUCT_CATEGORIES)


class Order(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)


class Basket(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)