# Generated by Django 3.2.5 on 2021-07-27 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Toppings',
            new_name='Topping',
        ),
    ]
