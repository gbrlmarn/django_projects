from django.shortcuts import render

from .models import Pizza

def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas' : pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    topping = pizza.topping_set.order_by('name')
    context = {'pizza' : pizza, 'topping' : topping}
    return render(request, 'pizzas/pizza.html', context)