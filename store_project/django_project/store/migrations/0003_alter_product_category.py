# Generated by Django 5.0.4 on 2024-06-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_bread_type_order_basket_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.PositiveIntegerField(choices=[(1, 'Dairy'), (2, 'Bread'), (3, 'Meat'), (4, 'Fish/Seafood'), (5, 'Drinks'), (6, 'Snacks'), (7, 'Tea/Coffee'), (8, 'Species/Sauces'), (9, 'Ceareals')]),
        ),
    ]
